book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"
book_info_list = book_info.split(" ; ")
name = book_info_list[0]
title = book_info_list[1]
year = book_info_list[2]
doi = book_info_list[3]
pages = book_info_list[4]
price = book_info_list[5]
f_name = name.title().strip()
f_title = title.title().strip()
f_doi = doi.replace("ISN","ISBN")
# f_price = 
# print(f_title)

print(f'The book {f_title} was written by {f_name} and published in {year}. It has {pages} pages and {f_doi} and costs ₦{price}.')