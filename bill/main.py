import vendor
import vendorBankAccount
import utility as util
import transactions

util.login()
vend = vendor.Vendor(name="Pera",
                     accNumber="1566",
                     address1="1234 Happy Lane",
                     addressCity="Santa Clara",
                     addressState="CA",
                     addressZip="95050",
                     addressCountry="USA")
vend.create()
vendorBankAccount = vendorBankAccount.VendorBankAccount(vend.id, vend.accNumber, "121000358", util.USERS_ID)
vendorBankAccount.create()
bill = transactions.Bill(vend.id, "14800", "2016-12-08", "2016-12-10",
                         billLineItems=[transactions.BillLineItem(1), transactions.BillLineItem(1)])
bill.create()

dict = {}
dict['billId'] = "00n01VTTHIHRKAKA7h37"
dict['amount'] = bill.amount
paybills = transactions.PayBills("00901HVFWIFCJEIP6s3i", "bac01RAZFDOIJJZF2dli", processDate="2021-09-23", billPays=[dict])
paybills.create()

recItems = transactions.RecurringBillItem(1)
rec = transactions.RecurringBill(vend.id, "2", 1, "2022-01-05", 1, [recItems])
rec.create()
