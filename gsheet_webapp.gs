// Web app for gsheet_sync.py. Deploy: Execute as = Me, Who has access = Anyone.
// Writes ONLY column I (result: text + font color + background) or column J (fix note: text only, u.col = 10)
// of the tab with the given gid, and only when the row's Execution.Key in column B matches. The token below
// must match GSHEET_TOKEN in .env.local.
var VERSION = 3;
var TOKEN = '8lMLAUhm2zPG-_HmpjxJseV-3_lPYrYF';

function doGet() {
  return out({v: VERSION});
}

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(30000);
  try {
    var body = JSON.parse(e.postData.contents);
    if (body.token !== TOKEN) return out({ok: false, error: 'unauthorized'});
    var sheet = SpreadsheetApp.getActive().getSheets().filter(function (s) { return s.getSheetId() === body.gid; })[0];
    if (!sheet) return out({ok: false, error: 'no tab with gid ' + body.gid});
    var mismatched = [], cells = [];
    body.updates.forEach(function (u) {
      if (String(sheet.getRange(u.row, 2).getValue()).trim() !== u.key) { mismatched.push(u.row + ':' + u.key); return; }
      var col = u.col === 10 ? 10 : 9;  // anything else falls back to the result column
      var cell = sheet.getRange(u.row, col).setValue(u.text);
      if (col === 9) cell.setFontColor(u.color).setBackground(u.background);  // null background clears the fill
      cells.push([u.row, col]);
    });
    SpreadsheetApp.flush();
    var values = {};
    cells.forEach(function (c) { values[c[0] + ':' + c[1]] = sheet.getRange(c[0], c[1]).getValue(); });
    return out({ok: true, v: VERSION, values: values, mismatched: mismatched});
  } catch (err) {
    return out({ok: false, error: String(err)});
  } finally {
    lock.releaseLock();
  }
}

function out(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
