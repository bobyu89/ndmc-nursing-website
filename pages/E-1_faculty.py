from components import (page, name_tape, statement, p, h4, text_link, actions, roster, back_to_top, facts,
                        draft, note)
from links import L
from tokens import C, S, SITE, TYPE

META = {"id": "E-1", "slug": "faculty", "title": "師資陣容", "owner": "院窗口"}

# 名單、職級、學位、專長逐字取自現行網站（2026-09-29 擷取）：
#   專任教師  https://wwwndmc.ndmutsgh.edu.tw/Doclist/191/100010/1738 及各教師 DocDet 個人頁
#   合聘教師  https://wwwndmc.ndmutsgh.edu.tw/Doclist/191/100010/721
#   兼任老師  https://wwwndmc.ndmutsgh.edu.tw/unit/100010/1470（114學年兼任老師名冊）
# 欄位缺漏者留空，不補寫。分組與排序照現行網站。

DOC = SITE + "/DocDet/191/100010/1738/"

# (分組, 姓名, 職級, 職務, 最高學位, 專長學科, 研究室或個人頁連結)
FULLTIME = [
    ("院長", "曾雯琦", "特聘教授", "院長", "美國加州大學舊金山分校護理哲學博士",
     "精神衛生護理", "https://sites.google.com/view/wctzeng/home"),
    ("系所主管", "林佳慧", "教授", "護理學系主任", "國防醫學院醫學科學研究所護理組博士",
     "內外科護理、護理行政管理、慢性病護理、健康促進、運動訓練、心肺復健、智慧醫療",
     "https://sites.google.com/view/linchiahuei/"),
    ("系所主管", "潘雪幸", "教授", "護理研究所所長", "國防醫學院醫學科學研究所護理組博士",
     "癌症護理、安寧療護、護理教育、急重症護理、軍陣護理", "https://sites.google.com/view/hhpndmc/home"),
    ("教授", "廖珍娟", "特聘教授", "", "美國華盛頓大學護理哲學博士",
     "建置癌症兒童及父母智慧化全人健康照護平台以提升其身心靈社會健康；孕期網路正念介入對孕婦身心社會健康；"
     "早產兒行為觀察、早產兒疼痛及睡眠；早產兒發展支持性介入；重症病人及家庭心理社會支持；孕婦紓壓介入；"
     "臨終家庭關懷；以能力為基礎之護理教育；反思性教學；翻轉教學；應用正念APP及聊天機器人舒壓及改善睡眠品質；"
     "創造產科護理暨實習之多模式人工智慧學習環境", DOC + "1658"),
    ("教授", "陳玉如", "教授", "", "美國亞歷桑那大學護理哲學博士",
     "成人護理學、重症護理學、損傷機轉與生物行為反應、生物回饋", DOC + "1656"),
    ("教授", "江慧珣", "教授", "", "國立台灣師範大學 健康促進與衛生教育學博士",
     "急診護理、災難護理、健康促進、創傷性腦損傷與遠距醫療",
     "https://sites.google.com/view/hui-hsunchiangndmc/h-ted-lab"),
    ("副教授", "梁鈞瑜", "副教授", "", "國防醫學院醫學科學研究所護理組博士",
     "燒傷護理、重症護理、負壓隔離病患護理、老人護理", DOC + "1661"),
    ("副教授", "王蔚芸", "副教授", "三軍總醫院護理部副主任", "國防醫學院醫學科學研究所護理組博士",
     "內外科護理、急診護理、症狀評估、健康管理、創新護理教育", "https://sites.google.com/view/wywang"),
    ("副教授", "楊佩陵", "副教授", "", "美國西雅圖華盛頓大學護理哲學博士",
     "睡眠、心理壓力調適、生理節律、症狀護理", DOC + "2720"),
    ("副教授", "藍湘勻", "副教授", "", "國防醫學大學醫學科學研究所護理組博士",
     "兒科護理、產科護理、軍陣暨災難護理、癌症護理、癌症兒童睡眠、早產兒及照顧者睡眠與壓力、軍校學生/醫事人員身心健康",
     "https://sites.google.com/view/hsiang-yun-lan-lab-ndmc/lab"),
    ("副教授", "林挺廸", "副教授", "", "美國伊利諾大學芝加哥分校護理哲學博士",
     "社區衛生護理、職業衛生護理、輪班工作者健康行為、工作壓力源、即時生態評估研究", DOC + "1666"),
    ("副教授", "馮欣蓓", draft("副教授"), "", "國防醫學院醫學科學研究所護理組博士",
     "精神科護理、質量性研究、大數據分析", DOC + "4036"),
    ("助理教授", "楊嘉禎", "助理教授", "", "長庚大學臨床醫學研究所博士",
     "內外科護理學、重症護理學、胸腔護理學、健康促進、吸菸行為", DOC + "1664"),
    ("助理教授", "莊蕙婉", "助理教授", "三軍總醫院護理部督導長", "國防醫學院醫學科學研究所護理組博士",
     "健康促進、高齡照護、內外科護理、急重症護理等相關研究", DOC + "3713"),
    ("助理教授", "蔡育倫", "助理教授", "三軍總醫院護理部督導長", "國防醫學院醫學科學研究所護理組博士",
     "護理倫理、安寧療護、全人護理等相關研究", DOC + "3853"),
    ("助理教授", "宋建美", "助理教授", "", "臺北醫學大學護理學系博士",
     "內外科護理、急重症護理、老人護理、護理行政、認知訓練、3D列印、專科護理師",
     "https://bobyu89.github.io/sung-lab-website/index.html"),
    ("助理教授", "林辰禧", "助理教授", "", "美國加州大學舊金山分校護理博士",
     "產科護理、婦女健康、內外科護理、重症護理", DOC + "1667"),
    ("助理教授", "賀彥中", "助理教授", "", "臺北醫學大學護理學系博士",
     "精神衛生護理學、數位化心理監測工具、量性研究、憂鬱症之長期監測、工具建構、長期追蹤資料分析、軌跡分析",
     "https://bobyu89.github.io/ycho-lab-website/index.html"),
    ("助理教授", "陳芃橋", "助理教授", "", "國立陽明交通大學護理實務博士 (Doctor of Nursing Practice, DNP)",
     "成人內外科護理、心血管疾病病人護理、自我照顧、健康促進、虛擬護理教育、量性研究、實證轉譯", DOC + "4540"),
    ("助理教授", "黃琬婷", "助理教授", "", "國立陽明交通大學護理學系博士 (Ph.D.)",
     "內外科護理學、心血管疾病照護、心臟復健、慢性病照護", "https://sites.google.com/view/wantinghuang"),
    ("助理教授", "劉育秀", "助理教授", "", "國立陽明交通大學護理學博士 (Ph.D.)",
     "兒科急重症及慢性病照護、先天性心臟病、恆毅力、質量性研究、專科護理師", "https://sites.google.com/view/ysliutw/"),
    ("講師", "林巧軒", "講師", "", "國防醫學院護理研究所婦兒組碩士",
     "產兒科護理、急重症護理、精神科護理", DOC + "3770"),
    ("講師", "宋皆儀", "講師", "", "國防醫學院護理研究所成人暨老人組碩士",
     "內外科護理學、重症護理學、心臟血管護理", DOC + "3769"),
    ("講師", "饒珮平", "講師", "", "國防醫學大學護理學院護理研究所碩士",
     "內外科護理、急重症護理", DOC + "4356"),
    ("助教", "陳姿吟", "助教", "", "", "", DOC + "3887"),
    ("助教", "伍哲君", "助理研究員", "", "國防醫學大學護理學院護理研究所碩士",
     "精神衛生護理、急重症護理", DOC + "4523"),
    ("助教", "黃敬雯", "助理研究員", "", "國防醫學大學護理學院護理研究所碩士",
     "內外科護理、急診護理", DOC + "4524"),
    ("助教", "陳懿維", "助教", "", "", "", DOC + "4537"),
    ("助教", "林靜伶", "行政專員", "", "國防醫學院護理學系研究所碩士",
     "成人護理學、內外科護理學、老人護理、急重症護理", DOC + "4556"),
    ("助教", "卞鳳珍", "助教", "", "", "", DOC + "1668"),
]

JOINT = [
    ("合聘", "王桂芸", "合聘教授", "瑞光健康科技總監暨教授", "國立師範大學健康促進與衛生教育學系博士",
     "內外科護理、胸腔護理、癌症護理、慢性疾病護理、重症護理、健康促進、衛生教育、介入性研究",
     SITE + "/DocDet/191/100010/721/1232"),
]

# 教師照片取自各教師現行 DocDet 個人頁的大頭照（2026-10-01 逐一確認 200 image/*）；楊嘉禎、陳姿吟、陳懿維個人頁沒有照片。
PHOTO = {
    "陳玉如": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E9%99%B3%E7%8E%89%E5%A6%82.png",
    "廖珍娟": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E5%BB%96%E7%8F%8D%E5%A8%9F2.jpg",
    "曾雯琦": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E6%9B%BE%E9%9B%AF%E7%90%A6.jpg",
    "梁鈞瑜": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E6%A2%81%E9%88%9E%E7%91%9C2.jpg",
    "潘雪幸": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E6%BD%98113%E5%B8%AB%E8%B3%87.jpg",
    "藍湘勻": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E8%97%8D%E8%80%81%E5%B8%AB112.png",
    "林挺廸": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E6%9E%97%E6%8C%BA%E5%BB%B8.jpg",
    "林辰禧": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E6%9E%97%E8%BE%B0%E7%A6%A7.jpg",
    "卞鳳珍": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E9%B3%B3%E7%8F%8D%E5%AD%B8%E5%A7%8A.JPG",
    "楊佩陵": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E6%A5%8A%E4%BD%A9%E9%99%B5%E8%BB%8D.jpg",
    "林佳慧": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E6%9E%97%E4%BD%B3%E6%85%A71130221.jpg",
    "莊蕙婉": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E8%8E%8A%E8%95%99%E5%A9%89112.jpg",
    "宋皆儀": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E5%AE%8B%E7%9A%86%E5%84%80112.10.jpg",
    "林巧軒": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E6%9E%97%E5%B7%A7%E8%BB%92112.10.5.jpg",
    "王蔚芸": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E7%8E%8B%E8%94%9A%E8%8A%B8_%E5%A4%A7%E9%A0%AD%E7%85%A7%E7%B6%B2%E9%A0%81%E6%AA%94.jpg",
    "蔡育倫": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E8%94%A1%E8%82%B2%E5%80%AB113.6.jpg",
    "馮欣蓓": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E9%A6%AE%E6%AC%A3%E8%93%93.jpg",
    "宋建美": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E5%AE%8B%E5%BB%BA%E7%BE%8E.jpg",
    "江慧珣": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/Chiang%2C%20Hui-Hsun%20Photo.jpeg",
    "饒珮平": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/IMG_5151.JPG",
    "賀彥中": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E8%B3%80%E5%BD%A5%E4%B8%AD.jpg",
    "伍哲君": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E4%BC%8D%E5%93%B2%E5%90%9B.jpg",
    "黃敬雯": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E9%BB%83%E6%95%AC%E9%9B%AF.jpg",
    "陳芃橋": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E9%99%B3%E8%8A%83%E6%A9%8B.jpg",
    "黃琬婷": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E9%BB%83%E7%90%AC%E5%A9%B7.png",
    "劉育秀": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E5%8A%89%E8%82%B2%E7%A7%80.jpg",
    "林靜伶": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/1738/%E6%9E%97%E9%9D%9C%E4%BC%B6jpg.jpg",
    "王桂芸": "https://wwwndmc.ndmutsgh.edu.tw/files/web/192/doctor/100010/721/%E7%8E%8B%E6%A1%82%E8%8A%B8.jpg",
}

GROUPS = ["院長", "系所主管", "教授", "副教授", "助理教授", "講師", "助教"]

# (兼聘等級, 姓名, 講授科目) — 114學年兼任老師名冊，原順序
ADJUNCT = [
    ('教授', '李選', '護理哲理與理論發展、護理專業問題專論、護理學導論、領導與管理'),
    ('助理教授', '朱珮儀', '進階軍陣護理'),
    ('助理教授', '李佳晏', '護理研究導論'),
    ('助理教授', '張傳馨', '臨床藥理及治療學'),
    ('講師', '高玉玲', '護理專業問題專論、精神衛生護理學'),
    ('講師', '李秀如', '精神衛生護理學實習'),
    ('講師', '蘇貞云', '內外科護理學實習'),
    ('講師', '鄭麗萍', '產科護理學實習'),
    ('講師', '胡子琳', '產科護理學實習、兒科護理學實習'),
    ('講師', '黃于芳', '基本護理學實習'),
    ('講師', '葉爵榮', '臨床藥理及治療學'),
    ('講師', '林潔盈', '產科護理學實習'),
    ('講師', '祝惠霖', '產科護理學實習'),
    ('講師', '柯盈萱', '進階專科護理學實習(二)、進階專科護理學實習(一)、進階專科護理學實習(三)'),
    ('講師', '粘乃欣', '內外科護理學實習'),
    ('講師', '陳怡如', '產科護理學實習'),
    ('講師', '林百慧', '內外科護理學實習'),
    ('講師', '謝珮琦', '內外科護理學實習'),
    ('講師', '張歆亞', '社區衛生護理學實習'),
    ('講師', '黃稜婷', '產科護理學實習'),
    ('講師', '望舒涵', '綜合臨床護理學實習(二)'),
    ('講師', '孫志琪', '產科護理學實習'),
    ('講師', '夏惠珍', '產科護理學實習'),
    ('教授', '郭羽倩', '兒科護理學實習'),
    ('講師', '顏毓嫻', '社區衛生護理學實習'),
    ('講師', '顏于惠', '綜合臨床護理學實習(二)'),
    ('講師', '楊捷安', '社區衛生護理學實習'),
    ('講師', '謝采汝', '兒科護理學實習'),
    ('講師', '丁可琁', '兒科護理學實習'),
    ('講師', '鍾承庭', '產科護理學實習'),
    ('講師', '周怡如', '精神衛生護理學實習'),
    ('講師', '李艾', '綜合臨床護理學實習(二)'),
    ('教授', '尹祚芊', '護理專業問題專論、護理學導論、社區衛生護理學、護理專業問題研討'),
    ('教授', '張玉坤', '進階資料分析方法論'),
    ('教授', '盧孳艷', '護理哲理與理論發展、質性研究'),
    ('副教授', '顧艷秋', '護理學導論、護理倫理學研討、領導與管理、護理專業問題研討'),
    ('副教授', '張鐸嚴', '教學原理與方法'),
    ('副教授', '尹玓', '產科護理學、兒科護理學、人類發展學實習'),
    ('助理教授', '呂偉明', '臨床藥理及治療學'),
    ('助理教授', '馮容莊', '產科護理學、護理資訊導論'),
    ('助理教授', '酒小蕙', '護理專業問題專論、社區衛生護理學、護理倫理學'),
    ('助理教授', '張玲華', '護理專業問題專論、護理行政概論、護理專業問題研討'),
    ('助理教授', '陳淑芬', '護理專業問題專論、產科護理學、人類發展學、護理倫理學'),
    ('助理教授', '洪世欣', '護理行政概論實習'),
    ('助理教授', '劉盈君', '精神衛生護理學、護理倫理學研討、質性研究、團體治療'),
    ('助理教授', '劉永芳', '內外科護理學、護理行政概論'),
    ('助理教授', '李春蘭', '護理行政概論、護理倫理學'),
    ('助理教授', '戰臨茜', '營養學、疾病營養學'),
    ('助理教授', '楊美紅', '領導與管理、內外科護理學、護理倫理學、護理專業問題研討'),
    ('助理教授', '李淑燕', '綜合臨床護理學實習(一)、護理行政概論實習'),
    ('助理教授', '林利珍', '護理研究導論、人類發展學、內外科護理'),
    ('助理教授', '楊寶寶', '臨床藥理及治療學'),
    ('助理教授', '陳美容', '護理行政概論、護理專業問題研討'),
    ('助理教授', '劉政宗', '臨床藥理及治療學'),
    ('助理教授', '楊嘉禎', '進階軍陣護理、進階實證護理學(二)'),
    ('助理教授', '蔣凱若', '進階精神衛生護理學(一)、進階精神衛生護理學(二)'),
    ('助理教授', '蕭鵬卿', '綜合臨床護理學實習(一)、護理行政概論實習'),
    ('助理教授', '吳毓慧', '綜合臨床護理學實習(一)'),
    ('助理教授', '廖家惠', '進階實證護理學(一)、進階實證護理學(二)'),
    ('助理教授', '吳莉芬', '綜合臨床護理學實習(一)'),
    ('講師', '張秉宜', '護理研究導論'),
    ('講師', '鄭淑琴', '精神衛生護理學實習'),
    ('講師', '賴惠娟', '綜合臨床護理學實習(一)、基本護理學實習'),
    ('講師', '鄭朝惠', '基本護理學實習'),
    ('講師', '李宜恬', '內外科護理學實習'),
    ('講師', '王琪', '產科護理學實習'),
    ('講師', '林妙怜', '兒科護理學實習'),
    ('講師', '戴美芬', '內外科護理學實習'),
    ('講師', '王媛', '產科護理學實習'),
    ('講師', '洪大恩', '軍陣護理學'),
    ('講師', '莊秋萍', '產科護理學實習'),
    ('講師', '劉建宏', '精神衛生護理學實習'),
    ('講師', '黃茱楹', '內外科護理學實習'),
    ('講師', '萬義康', '綜合臨床護理學實習(一)、綜合臨床護理學實習(二)'),
    ('講師', '蔡雨涵', '綜合臨床護理學實習(一)'),
    ('講師', '吳姿穎', '基本護理學實習'),
    ('講師', '陳冠戎', '綜合臨床護理學實習(一)'),
    ('講師', '陳誼珮', '兒科護理學實習'),
    ('講師', '林思妤', '產科護理學實習'),
    ('講師', '李旻苙', '精神衛生護理學實習'),
    ('講師', '游佩珊', '內外科護理學實習'),
    ('講師', '傅喻萱', '內外科護理學實習'),
    ('講師', '黃品瑄', '社區衛生護理學、社區衛生護理學實習'),
    ('講師', '洪繹雁', '兒科護理學實習'),
    ('講師', '馬景圓', '綜合臨床護理學實習(一)、內外科護理學實習'),
    ('講師', '蔡幸芳', '綜合臨床護理學實習(二)'),
    ('講師', '陳威呈', '兒科護理學實習'),
    ('講師', '江庭瑜', '綜合臨床護理學實習(一)、內外科護理學實習'),
    ('講師', '王儷諭', '產科護理學實習'),
    ('講師', '黃廷宇', '兒科護理學實習'),
    ('講師', '蕭雅文', '綜合臨床護理學實習(一)、基本護理學實習'),
    ('講師', '曾新雅', '綜合臨床護理學實習(一)、內外科護理學實習'),
    ('教授', '蔣立琦', '進階研究方法、進階實證護理學（二）'),
    ('講師', '林瑟華', '人類發展學實習'),
    ('講師', '陳妙儀', '進階專科護理學實習(一)'),
]

ADJ_RANKS = ["教授", "副教授", "助理教授", "講師"]

# 依專長找老師：分組只依本頁「專長學科」欄的原字詞——專長欄出現任一關鍵詞即列入該組，一位老師可同列多組。
# 只列教學職（院長至講師）與合聘教師；「助教」分組不列。英文頁 en_college_D-1 用同一套分組。
SPECIALTY = [
    ("內外科與成人護理", ["內外科", "成人", "胸腔", "心血管", "心臟血管", "燒傷"]),
    ("重症、急重症與急診", ["重症", "急診"]),
    ("婦兒護理", ["產科", "產兒科", "兒科", "早產兒", "孕", "婦女", "兒童"]),
    ("精神與心理衛生", ["精神", "心理", "憂鬱"]),
    ("癌症、安寧與臨終照護", ["癌症", "安寧", "臨終"]),
    ("社區、高齡與健康促進", ["社區", "職業衛生", "健康促進", "健康管理", "老人", "高齡"]),
    ("護理教育、行政與倫理", ["護理教育", "教學", "行政", "倫理"]),
    ("軍陣與災難護理", ["軍陣", "災難"]),
]


def specialty_groups(names):
    """[(組名, [姓名, ...]), ...]：names 為要列的老師（依名冊順序），比對 FULLTIME/JOINT 的專長學科欄。"""
    spec = {x[1]: x[5] for x in FULLTIME + JOINT}
    return [(label, [n for n in names if any(k in spec[n] for k in keys)]) for label, keys in SPECIALTY]


def name_links(items, anchor="p"):
    """Same markup as components.roster_index, but each name carries its own row number: [(name, n), ...]."""
    return "".join(
        f'<a href="#{anchor}{n}" style="display:inline-block;min-height:44px;padding:10px 0;margin-right:{S[3]};'
        f'color:{C["thread"]};font-weight:700;text-decoration:underline;text-underline-offset:5px;">{name}</a>'
        for name, n in items)


def index_group(title, items, anchor="p"):
    """Specialty index group: small heading, then a wrap-line of name links."""
    return (f'<h4 style="margin:{S[3]} 0 0;color:{C["thread"]};font-size:18px;line-height:1.45;font-weight:800;">{title}</h4>'
            f'<div style="margin:0 0 {S[1]};max-width:44em;line-height:1.4;">{name_links(items, anchor)}</div>')


def rank_heading(title):
    """Heading of the secondary rank index: same size as a specialty group heading, set off by a dashed rule."""
    return (f'<h4 style="margin:{S[4]} 0 {S[1]};padding-top:{S[2]};border-top:1.5px dashed {C["rule"]};max-width:44em;'
            f'color:{C["thread"]};font-size:18px;line-height:1.45;font-weight:800;">{title}</h4>')


def rank_line(label, items, anchor="p"):
    """Secondary (rank) index: the group label sits inline before its names, one compact line per group."""
    return (f'<div style="margin:0;max-width:44em;line-height:1.4;">'
            f'<span style="display:inline-block;min-width:5.5em;margin-right:{S[2]};{TYPE["small"]}font-weight:700;'
            f'color:{C["ink_soft"]};">{label}</span>{name_links(items, anchor)}</div>')


def _anchor(id_):
    """Jump target for the in-page index (plain empty div with an id; CMS keeps id)."""
    return f'<div id="{id_}"></div>'


def _fields(degree, speciality):
    """Roster 'fields' cell: speciality first, highest degree beneath in secondary ink."""
    out = speciality
    if degree:
        out += (f'<span style="display:block;margin-top:2px;{TYPE["small"]}color:{C["ink_soft"]};">'
                f'{degree}</span>')
    return out


def _rows(people):
    return [(name, rank, role or "護理學院", _fields(degree, spec), href, PHOTO.get(name))
            for _g, name, rank, role, degree, spec, href in people]


def render():
    opening = "".join([
        statement(
            draft("教你的人，也在做研究。"),
            draft("護理學系與護理研究所共用同一群專任老師，另有合聘與兼任老師帶領專業課程與臨床實習。"
                  "點開研究室連結，可以看到每位老師正在做的研究。"),
        ),
        actions(text_link("專任教師", "#fulltime"), text_link("合聘教師", "#joint"),
                text_link("兼任教師", "#adjunct")),
        note("全院師資資料將以 Google 表單向每位老師收集：姓名、職級、學經歷、研究領域、代表著作、研究室連結、聯絡方式。"
             "收齊後替換本頁內容與照片。目前名單、職級、學位與專長逐字取自現行網站。"),
    ])

    # 名冊列 id 由 p1 起連號（每組 start 偏移），合聘教師接在專任之後；num 記下每位老師的列號供兩種索引共用。
    fulltime, index, start, num = [], [], 1, {}
    for g in GROUPS + ["合聘教師"]:
        people = _rows(JOINT if g == "合聘教師" else [x for x in FULLTIME if x[0] == g])
        num.update({row[0]: n for n, row in enumerate(people, start)})
        index.append(rank_line(g, [(row[0], n) for n, row in enumerate(people, start)]))
        if g != "合聘教師":
            fulltime.append(h4(g))
            fulltime.append(roster(people, anchor="p", start=start))
            fulltime.append(back_to_top())
        else:
            joint = roster(people, anchor="p", start=start)
        start += len(people)

    teachers = [x[1] for x in FULLTIME if x[0] != "助教"] + [x[1] for x in JOINT]
    by_specialty = [index_group(label, [(n, num[n]) for n in names]) for label, names in specialty_groups(teachers)]

    adjunct = []
    for r in ADJ_RANKS:
        rows = [(n, c) for rank, n, c in ADJUNCT if rank == r]
        adjunct.append(h4(r))
        adjunct.append(facts(rows))
        adjunct.append(back_to_top())

    return page(
        opening,
        name_tape("依專長找老師"),
        p("依各老師列出的專長分組，一位老師可能出現在幾個組；點姓名直接跳到該位老師。", muted=True),
        *by_specialty,
        rank_heading("依職級"),
        *index,
        p("兼任教師名冊依兼聘等級列在頁面後段。", muted=True),
        _anchor("fulltime"),
        name_tape("專任教師"),
        note("照片取自各教師現行個人頁；楊嘉禎、陳姿吟、陳懿維個人頁沒有照片，請補。"
             "馮欣蓓老師職級：名單與個人頁標題寫副教授，個人頁內文寫「國防醫學大學護理學院助理教授」，"
             "學院最新消息 2026/08/25「恭賀本學院馮欣蓓 教師 升等 副教授」；請確認後拿掉待確認並更新個人頁內文。"
             "「助教」分組照現行網站，其中伍哲君、黃敬雯個人頁職稱為助理研究員，林靜伶為行政專員。"),
        *fulltime,
        _anchor("joint"),
        name_tape("合聘教師"),
        joint,
        back_to_top(),
        _anchor("adjunct"),
        name_tape("兼任教師"),
        p("114學年兼任老師名冊"),
        p("依兼聘等級排列，右欄為講授科目。", muted=True),
        *adjunct,
        note("兼任名冊依學年更新；新學年名冊出來時整批替換。楊嘉禎老師同時列於專任與兼任名冊，照現行網站保留。"),
        name_tape("相關頁面"),
        actions(text_link("學術研究", L("E-2")), text_link("教師資格審查", L("H-1")),
                text_link("學術資源", L("E"))),
        owner=META["owner"],
    )
