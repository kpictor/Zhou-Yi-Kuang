#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0

import hashlib
import os
import random
import time


class 卦:
    def __init__(self, 卦名, 卦象, 六爻, 爻辞):
        self.卦名 = 卦名
        self.卦象 = 卦象
        self.六爻 = 六爻
        self.爻辞 = 爻辞


六十四卦 = [
    卦(
        '乾',
        '䷀',
        ['阳爻', '阳爻', '阳爻', '阳爻', '阳爻', '阳爻'],
        [
            "元亨利贞",
            "初九潜龙勿用",
            "九二见龙在田利见大人",
            "九三君子终日乾乾夕惕若厉无咎",
            "九四或跃在渊无咎",
            "九五飞龙在天利见大人",
            "上九亢龙有悔",
            "用九见群龙无首吉",
        ]),
    卦(
        '坤',
        '䷁',
        ['阴爻', '阴爻', '阴爻', '阴爻', '阴爻', '阴爻'],
        [
            "元亨利牝马之贞君子有攸往先迷后得主利西南得朋东北丧朋安贞吉",
            "初六履霜坚冰至",
            "六二直方大不习无不利",
            "六三含章可贞或从王事无成有终",
            "六四括囊无咎无誉",
            "六五黄裳元吉",
            "上六龙战于野其血玄黄",
            "用六利永贞",
        ]),
    卦(
        '屯　',
        '䷂',
        ["阳爻", "阴爻", "阴爻", "阴爻", "阳爻", "阴爻"],
        [
            "元亨利贞勿用有攸往利建侯",
            "初九磐桓利居贞利建侯",
            "六二屯如邅如乘马班如匪寇婚媾女子贞不字十年乃字",
            "六三即鹿无虞惟入于林中君子几不如舍往吝",
            "六四乘马班如求婚媾往吉无不利",
            "九五屯其膏；小贞吉大贞凶",
            "上六乘马班如泣血涟如",
        ],
    ),

    卦(
        '蒙　',
        '䷃',
        ["阴爻", "阳爻", "阴爻", "阴爻", "阴爻", "阳爻"],
        [
            "亨匪我求童蒙童蒙求我初筮告再三渎渎则不告利贞",
            "初六发蒙利用刑人用说桎梏以往吝",
            "九二包蒙吉纳妇吉子克家",
            "六三勿用取女见金夫不有躬无攸利",
            "六四困蒙吝",
            "六五童蒙吉",
            "上九击蒙不利为寇利御寇,",
        ],
    ),

    卦(
        '需　',
        '䷄',
        ["阳爻", "阳爻", "阳爻", "阴爻", "阳爻", "阴爻"],
        [
            "有孚光亨贞吉利涉大川",
            "初九需于郊利用恒无咎",
            "九二需于沙小有言终吉",
            "九三需于泥致寇至",
            "六四需于血出自穴",
            "九五需于酒食贞吉",
            "上六入于穴有不速之客三人来敬之终吉",
        ],
    ),

    卦(
        '讼　',
        '䷅',
        ["阴爻", "阳爻", "阴爻", "阳爻", "阳爻", "阳爻"],
        [
            "有孚窒惕中吉终凶利见大人不利涉大川",
            "初六不永所事小有言终吉",
            "九二不克讼归而逋其邑人三百户无眚",
            "六三食旧德贞厉终吉或从王事无成",
            "九四不克讼复即命渝安贞吉",
            "九五讼元吉",
            "上九或锡之鞶带终朝三褫之",
        ],
    ),

    卦(
        '师　',
        '䷆',
        ["阴爻", "阳爻", "阴爻", "阴爻", "阴爻", "阴爻"],
        [
            "贞丈人吉无咎",
            "初六师出以律否臧凶",
            "九二在师中吉无咎；王三锡命",
            "六三师或舆尸凶",
            "六四师左次无咎",
            "六五田有禽利执言无咎长子帅师弟子舆尸贞凶",
            "上六大君有命开国承家小人勿用",
        ],
    ),

    卦(
        '比　',
        '䷇',
        ["阴爻", "阴爻", "阴爻", "阴爻", "阳爻", "阴爻"],
        [
            "吉原筮元永贞无咎不宁方来后夫凶",
            "初六有孚比之无咎有孚盈缶终来有它吉",
            "六二比之自内贞吉",
            "六三比之匪人",
            "六四外比之贞吉",
            "九五显比王用三驱失前禽邑人不诫吉",
            "上六比之无首凶",
        ],
    ),

    卦(
        '小畜',
        '䷈',
        ["阳爻", "阳爻", "阳爻", "阴爻", "阳爻", "阳爻"],
        [
            "亨密云不雨自我西郊",
            "初九复自道何其咎吉",
            "九二牵复吉",
            "九三舆说辐夫妻反目",
            "六四有孚血去惕出无咎",
            "九五有孚挛如富以其邻",
            "上九既雨既处尚德载妇贞厉月几望君子征凶",
        ],
    ),

    卦(
        '履　',
        '䷉',
        ["阳爻", "阳爻", "阴爻", "阳爻", "阳爻", "阳爻"],
        [
            "虎尾不咥人亨",
            "初九素履往无咎",
            "九二履道坦坦幽人贞吉",
            "六三眇能视跛能履履虎尾咥人凶武人为于大君",
            "九四履虎尾诉诉终吉",
            "九五夬履贞厉",
            "上九视履考祥其旋元吉",
        ],
    ),

    卦(
        '泰　',
        '䷊',
        ["阳爻", "阳爻", "阳爻", "阴爻", "阴爻", "阴爻"],
        [
            "小往大来吉亨",
            "初九拔茅茹以其汇征吉",
            "九二包荒用冯河不遐遗；朋亡得尚于中行",
            "九三无平不陂无往不复艰贞无咎勿恤其孚于食有福",
            "六四翩翩不富以其邻；不戒以孚",
            "六五帝乙归妹以祉元吉",
            "上六城复于隍勿用师自邑告命贞吝",
        ],
    ),

    卦(
        '否　',
        '䷋',
        ["阴爻", "阴爻", "阴爻", "阳爻", "阳爻", "阳爻"],
        [
            "之匪人不利君子贞大往小来",
            "初六拔茅茹以其汇贞吉亨",
            "六二包承小人吉大人否亨",
            "六三包羞",
            "九四有命无咎畴离祉",
            "九五休否大人吉其亡其亡系于苞桑",
            "上九倾否先否后喜",
        ],
    ),

    卦(
        '同人',
        '䷌',
        ["阳爻", "阴爻", "阳爻", "阳爻", "阳爻", "阳爻"],
        [
            "于野亨 利涉大川利君子贞",
            "初九同人于门无咎",
            "六二同人于宗吝",
            "九三伏戎于莽升其高陵三岁不兴",
            "九四乘其墉弗克攻吉",
            "九五同人先号啕而后笑大师克相遇",
            "上九同人于郊无悔",
        ],
    ),

    卦(
        '大有',
        '䷍',
        ["阳爻", "阳爻", "阳爻", "阳爻", "阴爻", "阳爻"],
        [
            "元亨",
            "初九无交害匪咎艰则无咎",
            "九二大车以载有攸往无咎",
            "九三公用亨于天子小人弗克",
            "九四匪其彭无咎",
            "六五厥孚交如威如；吉",
            "上九自天佑之吉无不利",
        ],
    ),

    卦(
        '谦　',
        '䷎',
        ["阴爻", "阴爻", "阳爻", "阴爻", "阴爻", "阴爻"],
        [
            "亨君子有终",
            "初六谦谦君子用涉大川吉",
            "六二鸣谦贞吉",
            "九三劳谦君子有终吉",
            "六四无不利㧑谦",
            "六五不富以其邻利用侵伐无不利",
            "上六鸣谦利用行师征邑国",
        ],
    ),

    卦(
        '豫　',
        '䷏',
        ["阴爻", "阴爻", "阴爻", "阳爻", "阴爻", "阴爻"],
        [
            "利建侯行师",
            "初六鸣豫凶",
            "六二介于石不终日贞吉",
            "六三盱豫悔迟有悔",
            "九四由豫大有得勿疑朋盍簪",
            "六五贞疾恒不死",
            "上六冥豫成有渝无咎",
        ],
    ),

    卦(
        '随　',
        '䷐',
        ["阳爻", "阴爻", "阴爻", "阳爻", "阳爻", "阴爻"],
        [
            "元亨利贞无咎",
            "初九官有渝贞吉出门交有功",
            "六二系小子失丈夫",
            "六三系丈夫失小子随有求得利居贞",
            "九四随有获贞凶有孚在道以明何咎",
            "九五孚于嘉吉",
            "上六拘系之乃从维之王用亨于西山",
        ],
    ),

    卦(
        '蛊　',
        '䷑',
        ["阴爻", "阳爻", "阳爻", "阴爻", "阴爻", "阳爻"],
        [
            "元亨利涉大川先甲三日后甲三日",
            "初六干父之蛊有子考无咎厉终吉",
            "九二干母之蛊不可贞",
            "九三干父之蛊小有悔无大咎",
            "六四裕父之蛊往见吝",
            "六五干父之蛊用誉",
            "上九不事王侯高尚其事",
        ],
    ),

    卦(
        '临　',
        '䷒',
        ["阳爻", "阳爻", "阴爻", "阴爻", "阴爻", "阴爻"],
        [
            "元亨利贞至于八月有凶",
            "初九咸临贞吉",
            "九二咸临吉无不利",
            "六三甘临无攸利既忧之无咎",
            "六四至临无咎",
            "六五知临大君之宜吉",
            "上六敦临吉无咎",
        ],
    ),

    卦(
        '观　',
        '䷓',
        ["阴爻", "阴爻", "阴爻", "阴爻", "阳爻", "阳爻"],
        [
            "盥而不荐有孚颙若",
            "初六童观小人无咎君子吝",
            "六二窥观利女贞",
            "六三观我生进退",
            "六四观国之光利用宾于王",
            "九五观我生君子无咎",
            "上九观其生君子无咎",
        ],
    ),

    卦(
        '噬嗑',
        '䷔',
        ["阳爻", "阴爻", "阴爻", "阳爻", "阴爻", "阳爻"],
        [
            "亨利用狱",
            "初九屦校灭趾无咎",
            "六二噬肤灭鼻无咎",
            "六三噬腊肉遇毒；小吝无咎",
            "九四噬干胏得金矢利艰贞吉",
            "六五噬干肉得黄金贞厉无咎",
            "上九何校灭耳凶",
        ],
    ),

    卦(
        '贲　',
        '䷕',
        ["阳爻", "阴爻", "阳爻", "阴爻", "阴爻", "阳爻"],
        [
            "亨小利有攸往",
            "初九贲其趾舍车而徒",
            "六二贲其须",
            "九三贲如濡如永贞吉",
            "六四贲如皤如白马翰如匪寇婚媾",
            "六五贲于丘园束帛戋戋吝终吉",
            "上九白贲无咎",
        ],
    ),

    卦(
        '剥　',
        '䷖',
        ["阴爻", "阴爻", "阴爻", "阴爻", "阴爻", "阳爻"],
        [
            "不利有攸往",
            "初六剥床以足蔑贞凶",
            "六二剥床以辨蔑贞凶",
            "六三剥之无咎",
            "六四剥床以肤凶",
            "六五贯鱼以宫人宠无不利",
            "上九硕果不食君子得舆小人剥庐",
        ],
    ),

    卦(
        '复　',
        '䷗',
        ["阳爻", "阴爻", "阴爻", "阴爻", "阴爻", "阴爻"],
        [
            "亨出入无疾朋来无咎反复其道七日来复利有攸往",
            "初九不复远无只悔元吉",
            "六二休复吉",
            "六三频复厉无咎",
            "六四中行独复",
            "六五敦复无悔",
            "上六迷复凶有灾眚用行师终有大败以其国君凶；至于十年不克征",
        ],
    ),

    卦(
        '无妄',
        '䷘',
        ["阳爻", "阴爻", "阴爻", "阳爻", "阳爻", "阳爻"],
        [
            "元亨利贞其匪正有眚不利有攸往",
            "初九无妄往吉",
            "六二不耕获不菑畬则利有攸往",
            "六三无妄之灾或系之牛行人之得邑人之灾",
            "九四可贞无咎",
            "九五无妄之疾勿药有喜",
            "上九无妄行有眚无攸利",
        ],
    ),

    卦(
        '大畜',
        '䷙',
        ["阳爻", "阳爻", "阳爻", "阴爻", "阴爻", "阳爻"],
        [
            "利贞不家食吉利涉大川",
            "初九有厉利已",
            "九二舆说輹",
            "九三良马逐利艰贞曰闲舆卫利有攸往",
            "六四童牛之牿元吉",
            "六五豮豕之牙吉",
            "上九何天之衢亨",
        ],
    ),

    卦(
        '颐　',
        '䷚',
        ["阳爻", "阴爻", "阴爻", "阴爻", "阴爻", "阳爻"],
        [
            "贞吉观颐自求口实",
            "初九舍尔灵龟观我朵颐凶",
            "六二颠颐拂经于丘颐征凶",
            "六三拂颐贞凶十年勿用无攸利",
            "六四颠颐吉虎视眈眈其欲逐逐无咎",
            "六五拂经居贞吉不可涉大川",
            "上九由颐厉吉利涉大川",
        ],
    ),

    卦(
        '大过',
        '䷛',
        ["阴爻", "阳爻", "阳爻", "阳爻", "阳爻", "阴爻"],
        [
            "栋桡利有攸往亨",
            "初六藉用白茅无咎",
            "九二枯杨生稊老夫得其女妻无不利",
            "九三栋桡凶",
            "九四栋隆吉有它吝",
            "九五枯杨生华老妇得其士夫无咎无誉",
            "上六过涉灭顶凶无咎",
        ],
    ),

    卦(
        '坎　',
        '䷜',
        ["阴爻", "阳爻", "阴爻", "阴爻", "阳爻", "阴爻"],
        [
            "习坎有孚维心亨行有尚",
            "初六习坎入于坎窞凶",
            "九二坎有险求小得",
            "六三来之坎坎险且枕入于坎窞勿用",
            "六四樽酒簋贰用缶纳约自牖终无咎",
            "九五坎不盈祗既平无咎",
            "上六系用徽𬙊寘于丛棘三岁不得凶",
        ],
    ),

    卦(
        '离　',
        '䷝',
        ["阳爻", "阴爻", "阳爻", "阳爻", "阴爻", "阳爻"],
        [
            "利贞亨畜牝牛吉",
            "初九履错然敬之无咎",
            "六二黄离元吉",
            "九三日昃之离不鼓缶而歌则大耋之嗟凶",
            "九四突如其来如焚如死如弃如",
            "六五出涕沱若戚嗟若吉",
            "上九王用出征有嘉折首获其匪丑无咎",
        ],
    ),

    卦(
        '咸　',
        '䷞',
        ["阴爻", "阴爻", "阳爻", "阳爻", "阳爻", "阴爻"],
        [
            "亨利贞取女吉",
            "初六咸其拇",
            "六二咸其腓凶居吉",
            "九三咸其股执其随往吝",
            "九四贞吉悔亡憧憧往来朋从尔思",
            "九五咸其脢无悔",
            "上六咸其辅颊舌",
        ],
    ),

    卦(
        '恒　',
        '䷟',
        ["阴爻", "阳爻", "阳爻", "阳爻", "阴爻", "阴爻"],
        [
            "亨无咎利贞利有攸往",
            "初六浚恒贞凶无攸利",
            "九二悔亡",
            "九三不恒其德或承之羞贞吝",
            "九四田无禽",
            "六五恒其德贞妇人吉夫子凶",
            "上六振恒凶",
        ],
    ),

    卦(
        '遁　',
        '䷠',
        ["阴爻", "阴爻", "阳爻", "阳爻", "阳爻", "阳爻"],
        [
            "亨小利贞",
            "初六遁尾厉勿用有攸往",
            "六二执之用黄牛之革莫之胜说",
            "九三系遁有疾厉畜臣妾吉",
            "九四好遁君子吉小人否",
            "九五嘉遁贞吉",
            "上九肥遁无不利",
        ],
    ),

    卦(
        '大壮',
        '䷡',
        ["阳爻", "阳爻", "阳爻", "阳爻", "阴爻", "阴爻"],
        [
            "利贞",
            "初九壮于趾征凶有孚",
            "九二贞吉",
            "九三小人用壮君子用罔贞厉羝羊触藩羸其角",
            "九四贞吉悔亡藩决不羸壮于大舆之輹",
            "六五丧羊于易无悔",
            "上六羝羊触藩不能退不能遂无攸利艰则吉",
        ],
    ),

    卦(
        '晋　',
        '䷢',
        ["阴爻", "阴爻", "阴爻", "阳爻", "阴爻", "阳爻"],
        [
            "康侯用锡马蕃庶昼日三接",
            "初六晋如摧如贞吉罔孚裕无咎",
            "六二晋如愁如贞吉受兹介福于其王母",
            "六三众允悔亡",
            "九四晋如鼫鼠贞厉",
            "六五悔亡失得勿恤往吉无不利",
            "上九晋其角维用伐邑厉吉无咎贞吝",
        ],
    ),

    卦(
        '明夷',
        '䷣',
        ["阳爻", "阴爻", "阳爻", "阴爻", "阴爻", "阴爻"],
        [
            "利艰贞",
            "初九明夷于飞垂其翼君子于行三日不食有攸往主人有言",
            "六二明夷夷于左股用拯马壮吉",
            "九三明夷于南狩得其大首不可疾贞",
            "六四入于左腹获明夷之心出于门庭",
            "六五箕子之明夷利贞",
            "上六不明晦初登于天后入于地",
        ],
    ),

    卦(
        '家人',
        '䷤',
        ["阳爻", "阴爻", "阳爻", "阴爻", "阳爻", "阳爻"],
        [
            "利女贞",
            "初九闲有家悔亡",
            "六二无攸遂在中馈贞吉",
            "九三家人嗃嗃悔厉吉；妇子嘻嘻终吝",
            "六四富家大吉",
            "九五王假有家勿恤吉",
            "上九有孚威如终吉",
        ],
    ),

    卦(
        '睽　',
        '䷥',
        ["阳爻", "阳爻", "阴爻", "阳爻", "阴爻", "阳爻"],
        [
            "小事吉",
            "初九悔亡丧马勿逐自复；见恶人无咎",
            "九二遇主于巷无咎",
            "六三见舆曳其牛掣其人天且劓无初有终",
            "九四睽孤遇元夫交孚厉无咎",
            "六五悔亡厥宗噬肤往何咎",
            "上九睽孤 见豕负涂载鬼一车 先张之弧后说之弧匪寇婚媾往遇雨则吉",
        ],
    ),

    卦(
        '蹇　',
        '䷦',
        ["阴爻", "阴爻", "阳爻", "阴爻", "阳爻", "阴爻"],
        [
            "利西南不利东北；利见大人贞吉",
            "初六往蹇来誉",
            "六二王臣蹇蹇匪躬之故",
            "九三往蹇来反",
            "六四往蹇来连",
            "九五大蹇朋来",
            "上六往蹇来硕吉；利见大人",
        ],
    ),

    卦(
        '解　',
        '䷧',
        ["阴爻", "阳爻", "阴爻", "阳爻", "阴爻", "阴爻"],
        [
            "利西南无所往其来复吉有攸往夙吉",
            "初六无咎",
            "九二田获三狐得黄矢贞吉",
            "六三负且乘致寇至贞吝",
            "九四解而拇朋至斯孚",
            "六五君子维有解吉；有孚于小人",
            "上六公用射隼于高墉之上获之无不利",
        ],
    ),

    卦(
        '损　',
        '䷨',
        ["阳爻", "阳爻", "阴爻", "阴爻", "阴爻", "阳爻"],
        [
            "有孚元吉无咎可贞利有攸往曷之用？二簋可用享",
            "初九已事遄往无咎酌损之",
            "九二利贞征凶弗损益之",
            "六三三人行则损一人；一人行则得其友",
            "六四损其疾使遄有喜无咎",
            "六五或益之十朋之龟弗克违元吉",
            "上九弗损益之无咎贞吉利有攸往得臣无家",
        ],
    ),

    卦(
        '益　',
        '䷩',
        ["阳爻", "阴爻", "阴爻", "阴爻", "阳爻", "阳爻"],
        [
            "利有攸往利涉大川",
            "初九利用为大作元吉无咎",
            "六二或益之十朋之龟弗克违永贞吉王用享于帝吉",
            "六三益之用凶事无咎有孚中行告公用圭",
            "六四中行告公从利用为依迁国",
            "九五有孚惠心勿问元吉有孚惠我德",
            "上九莫益之或击之立心勿恒凶",
        ],
    ),

    卦(
        '夬　',
        '䷪',
        ["阳爻", "阳爻", "阳爻", "阳爻", "阳爻", "阴爻"],
        [
            "扬于王庭孚号有厉告自邑不利即戎利有攸往",
            "初九壮于前趾往不胜为咎",
            "九二惕号莫夜有戎勿恤",
            "九三壮于頄有凶君子夬夬独行遇雨若濡有愠无咎",
            "九四臀无肤其行次且牵羊悔亡闻言不信",
            "九五苋陆夬夬中行无咎",
            "上六无号终有凶",
        ],
    ),

    卦(
        '姤　',
        '䷫',
        ["阴爻", "阳爻", "阳爻", "阳爻", "阳爻", "阳爻"],
        [
            "女壮勿用取女",
            "初六系于金柅贞吉有攸往见凶羸豕踟躅",
            "九二包有鱼无咎不利宾",
            "九三臀无肤其行次且厉无大咎",
            "九四包无鱼起凶",
            "九五以杞包瓜含章有陨自天",
            "上九姤其角吝无咎",
        ],
    ),

    卦(
        '萃　',
        '䷬',
        ["阴爻", "阴爻", "阴爻", "阳爻", "阳爻", "阴爻"],
        [
            "亨王假有庙利见大人亨利贞用大牲吉利有攸往",
            "初六有孚不终乃乱乃萃若号一握为笑勿恤往无咎",
            "六二引吉无咎孚乃利用禴",
            "六三萃如嗟如无攸利往无咎小吝",
            "九四大吉无咎",
            "九五萃有位无咎匪孚元永贞悔亡",
            "上六赍咨涕洟无咎",
        ],
    ),

    卦(
        '升　',
        '䷭',
        ["阴爻", "阳爻", "阳爻", "阴爻", "阴爻", "阴爻"],
        [
            "元亨用见大人勿恤南征吉",
            "初六允升大吉",
            "九二孚乃利用禴无咎",
            "九三升虚邑",
            "六四王用亨于岐山吉无咎",
            "六五贞吉升阶",
            "上六冥升利于不息之贞",
        ],
    ),

    卦(
        '困　',
        '䷮',
        ["阴爻", "阳爻", "阴爻", "阳爻", "阳爻", "阴爻"],
        [
            "亨贞大人吉无咎有言不信",
            "初六臀困于株木入于幽谷三岁不见",
            "九二困于酒食朱绂方来利用亨祀征凶无咎",
            "六三困于石据于蒺藜入于其宫不见其妻凶",
            "九四来徐徐困于金车吝有终",
            "九五劓刖困于赤绂乃徐有说利用祭祀",
            "上六困于葛藟于臲甈曰动悔有悔征吉",
        ],
    ),

    卦(
        '井　',
        '䷯',
        ["阴爻", "阳爻", "阳爻", "阴爻", "阳爻", "阴爻"],
        [
            "改邑不改井无丧无得往来井井汔至亦未繘井羸其瓶凶",
            "初六井泥不食旧井无禽",
            "九二井谷射鲋瓮敝漏",
            "九三井渫不食为我民恻可用汲王明并受其福",
            "六四井甃无咎",
            "九五井冽寒泉食",
            "上六井收勿幕有孚元吉",
        ],
    ),

    卦(
        '革　',
        '䷰',
        ["阳爻", "阴爻", "阳爻", "阳爻", "阳爻", "阴爻"],
        [
            "已日乃孚元亨利贞悔亡",
            "初九巩用黄牛之革",
            "六二已日乃革之征吉无咎",
            "九三征凶贞厉革言三就有孚",
            "九四悔亡有孚改命吉",
            "九五大人虎变未占有孚",
            "上六君子豹变小人革面征凶居贞吉",
        ],
    ),

    卦(
        '鼎　',
        '䷱',
        ["阴爻", "阳爻", "阳爻", "阳爻", "阴爻", "阳爻"],
        [
            "元吉亨",
            "初六鼎颠趾利出否得妾以其子无咎",
            "九二鼎有实我仇有疾不我能即吉",
            "九三鼎耳革其行塞雉膏不食方雨亏悔终吉",
            "九四鼎折足覆公𫗧其形渥凶",
            "六五鼎黄耳金铉利贞",
            "上九鼎玉铉大吉无不利",
        ],
    ),

    卦(
        '震　',
        '䷲',
        ["阳爻", "阴爻", "阴爻", "阳爻", "阴爻", "阴爻"],
        [
            "亨震来虩虩笑言哑哑震惊百里不丧匕鬯",
            "初九震来虩虩后笑言哑哑吉",
            "六二震来厉亿丧贝跻于九陵勿逐七日得",
            "六三震苏苏震行无眚",
            "九四震遂泥",
            "六五震往来厉亿无丧有事",
            "上六震索索视矍矍征凶震不于其躬于其邻无咎婚媾有言",
        ],
    ),

    卦(
        '艮　',
        '䷳',
        ["阴爻", "阴爻", "阳爻", "阴爻", "阴爻", "阳爻"],
        [
            "艮其背不获其身行其庭不见其人无咎",
            "初六艮其趾无咎利永贞",
            "六二艮其腓不拯其随其心不快",
            "九三艮其限列其夤厉熏心",
            "六四艮其身无咎",
            "六五艮其辅言有序悔亡",
            "上九敦艮吉",
        ],
    ),

    卦(
        '渐　',
        '䷴',
        ["阴爻", "阴爻", "阳爻", "阴爻", "阳爻", "阳爻"],
        [
            "女归吉利贞",
            "初六鸿渐于干小子厉有言无咎",
            "六二鸿渐于磐饮食衎衎吉",
            "九三鸿渐于陆夫征不复妇孕不育凶；利御寇",
            "六四鸿渐于木或得其桷无咎",
            "九五鸿渐于陵妇三岁不孕终莫之胜吉",
            "上九鸿渐于逵其羽可用为仪吉",
        ],
    ),

    卦(
        '归妹',
        '䷵',
        ["阳爻", "阳爻", "阴爻", "阳爻", "阴爻", "阴爻"],
        [
            "征凶无攸利",
            "初九归妹以娣跛能履征吉",
            "九二眇能视利幽人之贞",
            "六三归妹以须反归以娣",
            "九四归妹愆期迟归有时",
            "六五帝乙归妹其君之袂不如其娣之袂良月几望吉",
            "上六女承筐无实士刲羊无血无攸利",
        ],
    ),

    卦(
        '丰　',
        '䷶',
        ["阳爻", "阴爻", "阳爻", "阳爻", "阴爻", "阴爻"],
        [
            "亨王假之勿忧宜日中",
            "初九遇其配主虽旬无咎往有尚",
            "六二丰其蔀日中见斗往得疑疾有孚发若吉",
            "九三丰其沛日中见昧折其右肱无咎",
            "九四丰其蔀日中见斗遇其夷主吉",
            "六五来章有庆誉吉",
            "上六丰其屋蔀其家窥其户阒其无人三岁不见凶",
        ],
    ),

    卦(
        '旅　',
        '䷷',
        ["阴爻", "阴爻", "阳爻", "阳爻", "阴爻", "阳爻"],
        [
            "小亨旅贞吉",
            "初六旅琐琐斯其所取灾",
            "六二旅即次怀其资得童仆贞",
            "九三旅焚其次丧其童仆贞厉",
            "九四旅于处得其资斧我心不快",
            "六五射雉一矢亡终以誉命",
            "上九鸟焚其巢旅人先笑后号啕丧牛于易凶",
        ],
    ),

    卦(
        '巽　',
        '䷸',
        ["阴爻", "阳爻", "阳爻", "阴爻", "阳爻", "阳爻"],
        [
            "小亨利攸往利见大人",
            "初六进退利武人之贞",
            "九二巽在床下用史巫纷若吉无咎",
            "九三频巽吝",
            "六四悔亡田获三品",
            "九五贞吉悔亡无不利无初有终先庚三日后庚三日吉",
            "上九巽在床下丧其资斧贞凶",
        ],
    ),

    卦(
        '兑　',
        '䷹',
        ["阳爻", "阳爻", "阴爻", "阳爻", "阳爻", "阴爻"],
        [
            "亨利贞",
            "初九和兑吉",
            "九二孚兑吉悔亡",
            "六三来兑凶",
            "九四商兑未宁介疾有喜",
            "九五孚于剥有厉",
            "上六引兑",
        ],
    ),

    卦(
        '涣　',
        '䷺',
        ["阴爻", "阳爻", "阴爻", "阴爻", "阳爻", "阳爻"],
        [
            "亨王假有庙利涉大川利贞",
            "初六用拯马壮吉",
            "九二涣奔其机悔亡",
            "六三涣其躬无悔",
            "六四涣其群元吉涣有丘匪夷所思",
            "九五涣汗其大号涣王居无咎",
            "上九涣其血去逖出无咎",
        ],
    ),

    卦(
        '节　',
        '䷻',
        ["阳爻", "阳爻", "阴爻", "阴爻", "阳爻", "阴爻"],
        [
            "亨苦节不可贞",
            "初九不出户庭无咎",
            "九二不出门庭凶",
            "六三不节若则嗟若无咎",
            "六四安节亨",
            "九五甘节吉；往有尚",
            "上六苦节贞凶悔亡",
        ],
    ),

    卦(
        '中孚',
        '䷼',
        ["阳爻", "阳爻", "阴爻", "阴爻", "阳爻", "阳爻"],
        [
            "豚鱼吉利涉大川利贞",
            "初九虞吉有他不燕",
            "九二鸣鹤在阴其子和之我有好爵吾与尔靡之",
            "六三得敌或鼓或罢或泣或歌",
            "六四月几望马匹亡无咎",
            "九五有孚挛如无咎",
            "上九翰音登于天贞凶",
        ],
    ),

    卦(
        '小过',
        '䷽',
        ["阴爻", "阴爻", "阳爻", "阳爻", "阴爻", "阴爻"],
        [
            "亨利贞可小事不可大事飞鸟遗之音不宜上宜下大吉",
            "初六飞鸟以凶",
            "六二过其祖遇其妣；不及其君遇其臣；无咎",
            "九三弗过防之从或戕之凶",
            "九四无咎弗过遇之往厉必戒勿用永贞",
            "六五密云不雨自我西郊公弋取彼在穴",
            "上六弗遇过之飞鸟离之凶是谓灾眚",
        ],
    ),

    卦(
        '既济',
        '䷾',
        ["阳爻", "阴爻", "阳爻", "阴爻", "阳爻", "阴爻"],
        [
            "亨小利贞初吉终乱",
            "初九曳其轮濡其尾无咎",
            "六二妇丧其茀勿逐七日得",
            "九三高宗伐鬼方三年克之小人勿用",
            "六四𦈡有衣袽终日戒",
            "九五东邻杀牛不如西邻之禴祭实受其福",
            "上六濡其首厉",
        ],
    ),

    卦(
        '未济',
        '䷿',
        ["阴爻", "阳爻", "阴爻", "阳爻", "阴爻", "阳爻"],
        [
            "亨小狐汔济濡其尾无攸利",
            "初六濡其尾吝",
            "九二曳其轮贞吉",
            "六三未济征凶利涉大川",
            "九四贞吉悔亡震用伐鬼方三年有赏于大国",
            "六五贞吉无悔君子之光有孚吉",
            "上九有孚于饮酒无咎濡其首有孚失是",
        ],
    ),
]


class 爻:
    def __init__(self, origin, resolved, display):
        self.origin = origin
        self.resolved = resolved
        self.display = display

    def __repr__(self):
        return self.display

    def 为动爻(self):
        return self.origin != self.resolved

    def 为静爻(self):
        return not self.为动爻()


少阴 = 爻("阴爻", "阴爻", "⚋")
少阳 = 爻("阳爻", "阳爻", "⚊")
老阴 = 爻("阴爻", "阳爻", "⚋x")
老阳 = 爻("阳爻", "阴爻", "⚊o")


def 设置种子(占事):
    """
    设置起卦时的随机种子。
    """
    seed = int(hashlib.sha256(占事.encode()).hexdigest(), 16)
    seed += int.from_bytes(os.urandom(42), 'big')
    random.seed(seed)


def 摇卦():
    """
    以铜钱摇卦法摇卦，得到一爻。
    """
    # True 为正面，False 为背面。
    _ = input("请按 ENTER 键摇卦。")
    print("摇卦中...（请击掌两下摇卦）")
    time.sleep(1 + 1)  # 击掌两下摇卦
    result = [
        bool(random.getrandbits(1)),  # 第一枚铜钱
        bool(random.getrandbits(1)),  # 第二枚铜钱
        bool(random.getrandbits(1)),  # 第三枚铜钱
    ]
    print(('○' if result[0] else '●') + ('○' if result[1] else '●') + ('○' if result[2] else '●'))
    return [
        老阴,  # 三枚铜钱背面为老阴
        少阴,  # 两枚铜钱背面为少阴
        少阳,  # 两枚铜钱正面为少阳
        老阳,  # 三枚铜钱正面为老阳
    ][sum(result)]


if __name__ == '__main__':
    占事 = input('所问何事？\n')
    设置种子(占事)

    六爻 = []
    for _ in range(6):
        六爻.append(摇卦())
        当前卦象 = []
        for (i, 爻) in enumerate(六爻):
            当前卦象.append(f"第 {i + 1} 爻\t{爻}")
        当前卦象.reverse()
        print("\n".join(当前卦象))

    print("正在解卦...")
    time.sleep(5)

    动爻 = [(i, v) for (i, v) in enumerate(六爻) if v.为动爻()]
    静爻 = [(i, v) for (i, v) in enumerate(六爻) if v.为静爻()]
    本卦六爻 = [i.origin for i in 六爻]
    变卦六爻 = [i.resolved for i in 六爻]

    本卦 = next(filter(lambda x: x.六爻 == 本卦六爻, 六十四卦))
    变卦 = next(filter(lambda x: x.六爻 == 变卦六爻, 六十四卦))

    print(f"本卦\t{本卦.卦名}\t{本卦.卦象}")

    动爻之数 = len(动爻)
    卜辞 = None
    if 动爻之数 == 0:  # 六爻不变，以本卦卦辞断。
        卜辞 = 本卦.爻辞[0]
    elif 动爻之数 == 1:  # 一爻动，以动爻之爻辞断之。
        卜辞 = 本卦.爻辞[动爻[0][0] + 1]
    elif 动爻之数 == 2:  # 两爻动者，则取阴爻之爻辞以为断，盖以“阳主过去，阴主未来”故也。所动的两爻如果同是阳爻或阴爻，则取上动之爻断之。
        if 动爻[0][1].origin == '阴爻' and 动爻[1][1].origin == '阳爻':
            卜辞 = 本卦.爻辞[动爻[0][0] + 1]
        elif 动爻[1][1].origin == '阴爻' and 动爻[0][1].origin == '阳爻':
            卜辞 = 本卦.爻辞[动爻[1][0] + 1]
        else:
            卜辞 = 本卦.爻辞[动爻[1][0] + 1]
    elif 动爻之数 == 3:  # 三爻动者，以所动三爻的中间一爻之爻辞为断。
        卜辞 = 本卦.爻辞[动爻[1][0] + 1]
    elif 动爻之数 == 4:  # 四爻动者，以下静之爻辞断之。
        卜辞 = 本卦.爻辞[静爻[0][0] + 1]
    elif 动爻之数 == 5:  # 五爻动者，取静爻的爻辞断之。
        卜辞 = 本卦.爻辞[静爻[0][0] + 1]
    elif 动爻之数 == 6:  # 六爻皆动的卦，如果是乾坤二卦，「用」辞断。乾坤两卦外其余各卦，如果是六爻皆动，则以变卦的彖辞断之。
        if 本卦.卦名 == '乾':
            卜辞 = 本卦.爻辞[7]
        elif 本卦.卦名 == '坤':
            卜辞 = 本卦.爻辞[7]
        else:
            卜辞 = 变卦.爻辞[0]
            print(f"变卦\t{变卦.卦名}\t{变卦.卦象}")

    print(卜辞)
