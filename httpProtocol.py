# 2-http协议的组成，状态码含义

# HTTP 特点
# 1、支持客户/服务器模式；2、简便快速；3、灵活：4、无连接（每次连接只处理一个请求）；5、无状态。

# 2、HTTP之URL
# http://host[":"port][abs_path]
# 1. http —— 协议，http协议，定位网络资源
# 2. host —— internet 主机域名 或者 IP地址
# 3. port —— 端口，为空默认为80
# 4. abs_path —— 请求资源的 URI，未给以 ‘/’ 形式给出

# 3、HTTP之请求（Request）
# 由三部分组成，分别是：请求行（request line）、请求头（header）、请求正文
# 3.1 请求行（request line）：
# 请求方法 + URL + 协议版本 + 回车 + 换行（Method Request-URI HTTP-Version CRL）
# 3.1.1 请求方法
# 方法：get、post、head
# 3.2 请求头
# 3.3 请求正文

# 4、HTTP之响应（Response）
# 由三部分组成，分别是：状态行、消息报头、响应正文
# 4.1 状态行：
# 服务器HTTP协议的版本 + 响应状态码 + 状态码描述 (HTTP-Version Status-Code Reason-Phrase CRL)
# 4.1.1 响应状态码
# 4.1.1.1 1XX：指示信息--表示请求已接收，继续处理（100：继续，101：转换协议）
# 4.1.1.2 2xx：成功--表示请求已被成功接收、理解（200：请求成功，201：已创建，202：已接受未处理完成）
# 4.1.1.3 3xx：重定向--要完成请求必须进行更进一步的操作
# 4.1.1.4 4xx：客户端错误--请求有语法错误或请求无法实现（400：客户端请求的语法错误，服务器无法理解；
#                                                     401：请求要求用户的身份认证；404：无法找到资源；
#                                                     408：待客户端发送的请求时间过长，超时）
# 4.1.1.5 5xx：服务器端错误--服务器未能实现合法的请求（500：服务器内部错误，无法完成请求）