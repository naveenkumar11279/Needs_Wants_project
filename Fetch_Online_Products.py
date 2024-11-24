import requests
from bs4 import BeautifulSoup
o={}
from logger_config import get_logger
logger = get_logger("Fetch_Online_Products.py")
url= "https://www.amazon.in/Crucial-Basics-2666Mhz-Laptops-Notebooks/dp/B08BC2V71W/ref=pd_ci_mcx_mh_mcx_views_0_title?pd_rd_w=HHohO&content-id=amzn1.sym.fa0aca50-60f7-47ca-a90e-c40e2f4b46a9%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=fa0aca50-60f7-47ca-a90e-c40e2f4b46a9&pf_rd_r=4TA139T3HNXCZZ6QWNVE&pd_rd_wg=pBxrZ&pd_rd_r=4ce1fb29-0365-477e-8f3a-3642e8ab13d8&pd_rd_i=B08BC2V71W"

def get_amazon_product_mrp(url):
    # Define headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    # Send the HTTP GET request
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Failed to retrieve page. Status code: {response.status_code}"

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    # Find the MRP based on typical Amazon class names
    try:
        o["price"]=soup.find("span",{"class":"a-price"}).find("span").text
        # print(o)
        print("=>$ Found Price")
        logger.info("=>$ Found Price")
        return o
    except AttributeError:
        logger.info("MRP not found. Please check the HTML structure of the page.")
        print("MRP not found. Please check the HTML structure of the page.")
        logger.info(f"You have problem with this url: {url}")
        return 0
    except ValueError as e:
        print(f"we are not supposed to get this value : {e}")
        print(f"we are not supposed to get this value : so returning 0")
        logger.info(f"we are not supposed to get this value : so returning 0")
        return "0"


# Example: Replace with the actual Amazon product URL
print(get_amazon_product_mrp(url))
