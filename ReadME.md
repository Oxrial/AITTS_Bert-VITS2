## INFO

仓库文件基于@数列解析几何一生之敌 Bert-VITS2 2.1 整合包+@领航员未鸟自动标注

标注处理逻辑改造

### 0.VITS数据集批量重命名.bat

新增排序：在处理前生成临时目录信息文件并对文件按文件名中的数字排序
默认为最后一组数字
例：
	raw_audio
    	123_xxx_10.wav
    	123_xxx_103.wav
    	123_xxx_20.wav
    	123_xxx_205.wav

默认取 10 103... 作为排序基准，支持入参

监听排序执行完成之后才会进行文件名批量更改

修改【文件对照表.txt】的写入格式去除双引号方便重命名重置

### 1.带标点符号的标注.bat

根据Bert-VITS2_2.1实验文件夹路径调整filelists所需要的list文件内容格式（auto_DataLabeling_long.py）

新增排序：在生成txt，list前生成临时目录信息文件并对文件按文件名中的数字排序
默认为最后一组数字

### 2.清理用于Bert_VITS2的标注.bat

调整txt文件路径（clean_list.py）

### 3.undo_rename.bat（新增）

根据【文件对照表.txt】将raw_audio下的重命名wav音频文件名重置
