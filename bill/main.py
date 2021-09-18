import vendor
import vendorBankAccount
import utility as util
import transactions

util.login()
vend = vendor.Vendor(name="Pera", accNumber="1234567")
vend.create()
vendorBankAccount = vendorBankAccount.VendorBankAccount(vend.id, vend.accNumber, "121000358", util.USERS_ID)
vendorBankAccount.create()
bill = transactions.Bill(vend.id, "14800", "2016-12-05", "2016-12-07",
                         billLineItems=[transactions.BillLineItem(1500), transactions.BillLineItem(2000)])
bill.create()

dict = {}
dict['billId'] = bill.id
dict['amount'] = bill.amount

paybills = transactions.PayBills(vend.id, vendorBankAccount.id, billPays=[dict])
paybills.create()

recItems = transactions.RecurringBillItem(1000)
rec = transactions.RecurringBill(vend.id, "2", 1, "2022-01-05", 1, [recItems])
rec.create()
