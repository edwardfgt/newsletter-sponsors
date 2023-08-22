import gspread

sa = gspread.service_account(filename="sheets_secret.json")
sh = sa.open("Email Sponsors")
wks = sh.worksheet("Sponsors")

print("rows: ", wks.row_count)