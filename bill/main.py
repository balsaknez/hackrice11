import user
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

userProfile = user.UserProfile()
user = user.User(userProfile.getUserProfileId(), "Mika1111111", "Knezevic", "balsak97122111111@gmail.com")
user.create()

bill = transactions.Bill(user.id, vend.id, "14800", "2021-09-18", "2021-09-23",
                         billLineItems=[transactions.BillLineItem(1), transactions.BillLineItem(1)])
bill.create()



BALSA_ID = "00601GOONLKPXKHA3bwo"

# bill.setBillApprover(BALSA_ID)
# bill.setBillApproverPolicy(1, 1)

# dict = {}
# dict['billId'] = bill.id
# dict['amount'] = bill.amount
# paybills = transactions.PayBills(vend.id, "bac01MKKQWGBVJNF2dlj", processDate="2021-09-23", billPays=[dict])
# paybills.create()

# recItems = transactions.RecurringBillItem(1)
# rec = transactions.RecurringBill(vend.id, "2", 1, "2022-01-05", 1, [recItems])
# rec.create()

#print(vendor.Vendor.get_vendor_by_vendor_name("pera"))
print(transactions.Bill.billMap[bill.id])
print(user.id)
print(transactions.Bill.getBillsForUser(user.id, vend.id))

