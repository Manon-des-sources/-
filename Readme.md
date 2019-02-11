待开发功能：

* 1、在**协议数据帧窗口**选中协议数据后可以右键选择**按指定协议解析**：

    ![1001](Scripts\右键安指定协议解析.png)

* 2、增加协议

   打开一个选择协议的窗口：

   * 选项卡1：选择protocals目录下的协议文档
   * 选项卡2：打开协议编辑器开始编辑协议
     * 可以从空白开始编辑
     * 可以导入协议模板、在此基础上修改
     * 保存时就将这个协议文档和协议名称绑定、在上一步的协议列表中就会多一个协议名称
     * 也可以修改这个协议名称绑定的协议文档
     * 数据帧里面的每一项(标况、温度、...)
       * 可以直接拖动每一项来移动这一项在数据帧里面的位置
       * 每一项的数据长度可以直接修改
       * 每一项都可以选择数据类型和解析接口
         * 解析接口可以选择miniFuns目录下的python接口文件和c接口文件
         * 也可以打开接口编辑器编辑接口：
           * 绑定接口名称和接口文件
           * 直接书写python接口和C接口代码
           * 保存接口文件时只检查接口接口名称和接口参数(不保证接口文件的正确性)