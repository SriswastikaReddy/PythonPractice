#universal resource indicator
#https(protocol),kaggle(Domain)./datasets(address or name of a page)
#https://www.kaggle.com/datasets

url = input("enter a URL: ")
#protocol = (url.split("://")[0])
#domain = (url.split(".")[1])
#address = (url.rsplit('m',1)[1])
#print(f'protocol: {protocol}\ndomain: {domain}\naddress: {address}')

protocol = url[ :url.index(':')]
dot1 = url.find('.')
dot2 = url.find('.', dot1+1)
domain = url[dot1+1:dot2]
address = url[url.find('/',dot2): ]
print(f'protocol: {protocol}\ndomain: {domain}\naddress: {address}')
