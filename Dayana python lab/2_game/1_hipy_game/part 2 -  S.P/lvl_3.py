# The third stage of the second part
# In this part, you will be given all the necessary things to write the code. At this point, you are just a writer


# Expand the code from the previous step as follows
# expansion = develop

# Get the address of the page from the user. In addition, get a number as a degree or depth
# Re-download the page related to the link according to the number of degrees received for each link on the main page
# Then download all its links and put them in the same file, under the link set of the new page
# The text below is a quasi-code for your better understanding

# url = input("enter the url: ")
# degree = input("enter the degree: ")

# page_content = get_page_content_with_url(url)
# urls_of_page = get_page_urls_from_content(page_content)

# for each url_of_page in urls_of_page:
#   save url_of_page in a text file
#   if degree is not equal to 0:
#       for range 1 to degree:
#           go_and_get_linked_page_content and do this until you reach do given degree
#        
# Be careful that this is just a pseudo-code for your better understanding
# tips: for cleaner code, please use functions