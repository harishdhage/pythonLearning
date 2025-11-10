print("Bill Calculator")
total_bill = int(input("Total Bill amount : $"))
tip = int(input("Enter tip on bill : "))
bill_include_tip = total_bill + tip
total_num_ppl = int(input("Bill will be shared among : "))
print(f"Bill per person : ${round((bill_include_tip/total_num_ppl),2)}")