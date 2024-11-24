from Fetch_Online_Products import get_amazon_product_mrp
from Load_to_File import Price_writing_excel,write_to_DatawriteCell
from Get_Product_Links import Product_link_from_file,get_column_data_by_header
from logger_config import get_logger

logger = get_logger("Main.py")
logger.info("Application started. NOW")
file_path = r"D:\Needs&Wants.xlsx"
product_url = list(get_column_data_by_header(file_path,"Links").items())
for ind,url in product_url:
    print(url)
    writing_to_ind = ind.replace("F","E")
    if url is not None:
        logger.info("=>$ Getting Price of Product Loading...")
        Today_price_raw = get_amazon_product_mrp(url)
        logger.info("=>$ Getting Price of Product Loading...")
        print(Today_price_raw)
        try:
            Today_price=float(Today_price_raw['price'].replace("₹","").replace(",",""))
        except Exception as e:
            print(e)
            Today_price = 0
        # print(Today_price,"writing to => ",writing_to_ind)
        Price_writing_excel(Today_price,writing_to_ind)

if __name__ == '__main__':
    print('=>$Successfully Executed')
    logger.info("=>$Successfully Executed")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
