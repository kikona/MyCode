# 结构化文件存储
- xml, json
- 为了解决不同设备之间的信息交换问题
- xml：人可以读，但是有点啰嗦
- json：比xml简洁

# xml文件
- 参考资料：
    - https://docs.python.org/3/library/xml.etree.elementtree.html
    - http://www.runoob.com/python/python-xml.html
    - https://blog.csdn.net/seetheworld518/article/details/49535285
    
- XML:可扩展标记语言
    - 标记语言：语言中使用尖括号括起来的文本字符串标记
    - 可扩展：用户可以自己定义需要的标记
    - 例如：
            
            <Teacher>
                自定义标记Teacher
                在两个标记之间的 任何内容都应该跟Teacher相关
            </Teacher>
    - 是w3c组织制定的一个标准
    - XML描述的是数据本身，即数据的结构和语义
        - 而HTML侧重于如何显示web页面中的数据
    - 可以用浏览器查看xml文档
    
- XML文档的构成
    - 处理指令（可以认为一个文件内只有一个处理指令）
        - 最多只有一行，且必须在第一行
        - 内容是与xml本身一起处理一些声明或者指令
        - 以xml关键字开头，并且前后各有一个?
        - 一般用于声明XML的版本和采用的编码
            - version属性是必须的
            - encoding属性用来指出xml解释器使用的编码
    - 根元素（一个文件内只有一个根元素）
        - 在整个xml文件中，可以把它看做一个树形结构：即最外层只有一对尖括号
        - 根元素有且只有一个
    - 子元素
    - 属性
    - 内容
    - 注释
        
     