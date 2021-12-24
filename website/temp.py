# from random import choice
#
#
# with open("temp.txt", 'w') as fh:
#     for i in range(1, 12627):
#         month_payed = choice([10, 11, 12, 1, 2, 3])
#         print(month_payed)
#         stmt = f"INSERT INTO public.payments (month_payed, resident_id) VALUES ({month_payed}, {i});\n"
#         fh.write(stmt)
#
#
# fh.close()
