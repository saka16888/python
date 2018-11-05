
tmp=input().strip().split(' ')
arr_input = [int(arr_temp) for arr_temp in tmp]
n=arr_input[0]
k=arr_input[1]

tmp=input().strip().split(' ')
meal_input = [int(arr_temp) for arr_temp in tmp]
meal_no_share=meal_input[k]
print("meal_input = ",meal_input,"meal_no_share = ", meal_no_share)

tmp=input().strip().split(' ')
b_charge=int(tmp[0])

share = (sum(meal_input) - meal_no_share)/2

if (b_charge == share) :
    print("Bon Appetit")
else:
    print("%d" % (b_charge-share) )
