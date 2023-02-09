import streamlit as st

with st.sidebar:

    st.markdown("# [簡介](#簡介)")
    st.markdown("## [影片教學](#影片教學)")

st.title("CVAT 使用教學")
st.title("簡介")

st.markdown('''
**CVAT是一個OpenCV項目，可為電腦視覺數據集提供簡單的標記。CVAT 允許您利用易於使用的界面來簡化計算機視覺註釋。**

CVAT 是一個開放的標籤器，一個免費的開源標籤工具，一個免費的註釋器，一個圖像註釋器，當然還有一個計算機視覺註釋工具。CVAT 標籤支持的計算機視覺的常見用例是：圖像分類、對象檢測、對象跟踪、圖像分割和姿態估計。

**在這篇文章中，我們將重點介紹 CVAT 在圖像上進行==對象檢測==註釋的能力**，儘管它還有更多功能，包括用於視頻的 CVAT 註釋工具、用於語義分割的 CVAT 註釋工具、用於多邊形註釋的 CVAT 等等。

# 連線方式
### 使用 **Chrome** 瀏覽器輸入 ==**10.96.212.243:8080**==

**其他瀏覽器可能會造成不可預知的錯誤**
''')

st.image(r'.\doc\sQCOtu4.png')

st.markdown('''
# 影片教學
**在本視頻中，我們展示瞭如何使用 CVAT - 如何註冊、上傳數據、註釋和下載數據。**
該視頻是系列視頻中的第一個，將指導您了解我們的產品及其眾多功能。

**本平台採Offline方式架設 ==不會寄送驗證信件至您的郵箱，註冊完畢即可登入使用。==**
- **Email** 請填入 **公司 Mail**
- **Username** 請填入 **NT帳號**
- **Password** 需**長度大於8個字元**，並至少**包含一個大寫字元**
''')

st.video('https://www.youtube.com/watch?v=14Z1Ukynxd4')

st.markdown('''
**在以下視頻中，我們展示了在插值模式下標註如何顯著提高標註效率。這個過程很簡單，由三個簡單的步驟組成：**

- 建立框架步驟。
- 選擇形狀和標籤。
- 根據既定的幀步驟註釋幀。

然後 CVAT 將處理其餘部分，從而使註釋過程的速度提高 10 倍。

''')

st.video('https://www.youtube.com/watch?v=sA_H3EGzO60')

st.title('''# 創建任務''')

st.image(r'.\doc\NGYZ2Rr.png')

st.markdown('''

創建標註任務先了解**Project**、**task**與**Job**的差異

**Project** -- 在 CVAT，您可以創建一個包含相同類型任務的**Project**。與**Project**相關的所有**Task**都將繼承一個標籤列表。
```
- Project A
    - Task a
        - Job 1
        - Job 2
    - Task b
        - Job 3
```
## **Create Tasks**
**如何創建和配置註釋任務。**
要開始在 CVAT 中進行註釋，您需要創建一個註釋任務並指定其參數。

要創建任務，請在 **Tasks** 頁面上單擊 **+** 並選擇創建新任務。
''')

st.image(r'.\doc\8fw5JCb.png')

st.markdown('''

要創建新任務，請打開任務配置器：
''')

st.image(r'.\doc\BJzZKfD.png')

st.markdown('''

並指定以下參數：

1. 在`Name`字段中，輸入新任務的名稱。
2. （可選）從`Projects `下拉列表中，為新任務選擇一個項目。
如果您不想將任務分配給任何項目，請將此字段留空。
![](https://i.imgur.com/o5QcSwe.png)

3. 在**Constructor** 分頁, 點擊**Add label**.
    ![](https://i.imgur.com/SUYQmX6.png)

4. 在**Label name**中，輸入標籤的名稱。
    - **手動輸入**
        如需繼續輸入類別請按**Continue**，新增完畢點擊**Cancel**

    - **以 RAW 格式編輯標籤**
        **Raw**是一種為高級用戶處理標籤的方法。==**當您需要將標籤從一個獨立任務複製到另一個任務時，它很有用**==。
        ![](https://i.imgur.com/G1kliQ1.png)


6. （可選）要將標籤的使用限制為特定形狀工具，請從**Label shape**下拉列表中選擇形狀。
7. （可選）選擇標籤的顏色。
    ![](https://i.imgur.com/Az5UAl6.png)
7. （可選）單擊[**Add an attribute**](https://opencv.github.io/cvat/docs/manual/basics/create_an_annotation_task/#add-an-attribute)並設置其屬性。
8. 單擊**Select files**上傳文件進行註釋。
    **上傳文件有幾種方式：**
    - **My computer** 使用此選項從您的筆記本電腦或 PC 中選擇文件。==(因資安疑慮關閉該功能)==
    - **Connected file share** 使用此選項從共享文件夾上傳文件，**該資料夾與CCTV主機Z:\目錄公用**。

9. 點擊**Continue**提交標籤並開始添加新標籤或**Cancel**終止當前標籤並返回到標籤列表。
10. 點擊**Submit and open**以提交配置並打開創建的任務，或點擊提交**Submit and continue**以提交配置並啟動新任務。

## Tasks page
任務頁面概覽。
![](https://i.imgur.com/QyQG4GT.png)

任務頁面包含元素，每個元素都與一個單獨的任務相關。它們按創建順序排序。每個元素包含：任務名稱、預覽、進度條、按鈕`Open`和菜單`Actions`。每個按鈕負責菜單操作中的特定功能：

- `Export task dataset`——下載特定格式的註釋或註釋和圖像。[export/import datasets](https://opencv.github.io/cvat/docs/manual/advanced/export-import-datasets/) 提供了更多信息。
- `Upload annotation` 上傳註解以特定格式上傳註解。
- `Automatic Annotation` —— 使用工具包進行自動註釋 ==(請向管理員申請權限開啟此功能)==
    在運行時 - 您可以看到完成百分比。您可以通過單擊Cancel按鈕取消自動註釋。
    ![](https://i.imgur.com/LyKlMcO.png)

- `Backup task` —— 將此任務備份到 zip 存檔中。在[backup](https://opencv.github.io/cvat/docs/manual/advanced/backup/) 閱讀更多內容。
- `Move to project` —— 將任務移動到項目（可用於將任務從一個項目移動到另一個項目）。請注意，屬性會在移動過程中重置。如果標籤不匹配，您可以在項目/任務中創建或刪除必要的標籤。一些任務標籤可以與目標項目標籤相匹配。
- `Delete` — 刪除任務。

## Task details
任務詳細信息是一個任務頁面，其中包含預覽、進度條和任務詳細信息（在創建任務時指定）和作業部分。
![](https://i.imgur.com/tNxu5X5.png)


- **Jobs** — 是特定**Task**的所有作業的列表。在這裡您可以找到下一個資料：
- **Job#1234** — 帶有==超鏈接==的**Job**名稱.
- **Frames** — 幀間隔。
- **Stage** — 該階段由下拉列表指定。分為三個階段：`annotation`、`validation` 或 `acceptance`。該值影響任務進度條。
- **State** — 分配的用戶可以在作業內的菜單中更改狀態。有幾種可能的狀態：`new`、`in progress`、`rejected`、`completed`。
- **Started on** — 這項工作的開始日期。
- **Duration** — 是工作進行的時間量。
- **Assignee** — 是從事該工作的用戶。您可以開始輸入受讓人的姓名和/或從下拉列表中選擇合適的人。

**點擊 Job#1234 即可進入標註頁面**
![](https://i.imgur.com/SRErzFN.png)

# 基本元件
## 基本控件概述
1. 使用下面的箭頭移動到下一幀/上一幀。使用滾動條滑塊滾動幀。幾乎每個按鈕都有一個快捷方式。要獲得有關快捷方式的提示，只需將鼠標指針移到 UI 元素上即可。
![](https://i.imgur.com/ncOHvw7.png)

2. 要導航圖像，請使用控件側欄上的按鈕。移動/移動圖像的另一種方法是在沒有註釋對象的區域內按住鼠標左鍵。如果**Mouse Wheel**按下 ，則忽略所有帶註釋的對象。否則，將移動突出顯示的邊界框而不是圖像本身。
![](https://i.imgur.com/gBq8wHT.png)

3. 您可以使用側邊欄控件上的按鈕縮放感興趣的區域。使用 按鈕**Fit the image**使圖像適合工作區。您還可以使用鼠標滾輪縮放圖像（圖像將相對於您當前的光標位置縮放）。
4. ![](https://i.imgur.com/zBQxN4S.png)
---
## 頂部控制面板

![](https://i.imgur.com/XTuRybl.png)

- #### **MENU按鈕**
    是標註工具的主菜單。它可用於下載、上傳和刪除註釋。
    ![](https://i.imgur.com/QTW1tFY.png)


    - **Upload Annotations**——將註釋上傳到任務中。

    - **Export as a dataset **[受支持的格式](https://opencv.github.io/cvat/docs/manual/advanced/formats/)從任務中下載數據集。 如果您希望數據集包含圖像，您還可以輸入**自定義名稱**並啟用**保存圖像複選框。**

    - **Open the task** — 打開包含任務詳細信息的頁面。
    - **Change job state** - 更改作業的狀態 ( `new`, `in progress`, `rejected`, `completed`)。
    - **Finish the job** / **Renew the job** - 將作業階段和狀態相應地更改為`acceptance`和`completed`/`annotation`和`new`。

- ### **保存工作**
    保存當前作業的註釋。該按鈕具有保存過程的指示。

    **==長時間使用可能造成電腦記憶體不足==，保持隨手存檔好習慣**

    ![](https://i.imgur.com/MgGwxVW.png)

- ### **撤消重做按鈕**
    使用按鈕撤消操作或重做它們。
    ![](https://i.imgur.com/WqX9JGj.png)


- ### **完畢**
    用於完成對象的創建。此按鈕僅在創建對象時出現。
    ![](https://i.imgur.com/x9yOzTJ.png)

- ### 全屏播放器
    全屏播放器模式。鍵盤快捷鍵是F11。

    全屏播放==可加大標註區域更方便工作==，點擊**ESC**退出

    ![](https://i.imgur.com/uPwARlP.png)

## 控制側邊欄

- **Navigation**- 包含用於移動和旋轉圖像的工具。

    | 圖標 | 描述 |
    | ---- | ---- |
    | ![](https://opencv.github.io/cvat/images/image148.jpg) | `Cursor`( `Esc`)- 一個基本的註釋編輯工具。 |
    | ![](https://opencv.github.io/cvat/images/image149.jpg) | `Move the image`一種用於在無法編輯的情況下移動圖像的工具。 |
    | ![](https://opencv.github.io/cvat/images/image102.jpg) | `Rotate`順時針 ( `Ctrl+R`) 和逆時針 ( )旋轉當前幀的兩個按鈕`Ctrl+Shift+R`。 您可以`Rotate all images`在設置中啟用以旋

- **Zoom block** - 包含用於圖像縮放的工具。

    | 圖標 | 描述 |
    | ---- | ---- |
    | ![](https://opencv.github.io/cvat/images/image151.jpg) | `Fit image`- 使圖像適合工作區大小。 快捷方式——雙擊圖片 |
    | ![](https://opencv.github.io/cvat/images/image166.jpg) | `Select a region of interest`- 放大選定區域。 您可以使用此工具快速放大畫面的特定部分。 |

- **Shapes block**- 包含用於創建形狀的所有工具。

    現階段只會使用到以下三種工具，其他以後有機會再介紹。**Rectangle中的==Shape Mode==以及==Track Mode==會大量使用到建議仔細閱讀**。

    | 圖標 | 描述 | 鏈接到部分 。
    | ---- | ---- | ---- |
    | ![](https://opencv.github.io/cvat/images/image189.jpg) | `AI Tools` | [人工智能工具](#人工智能工具) |
    | ![](https://opencv.github.io/cvat/images/image201.jpg) | `OpenCV` | 	OpenCV|
    | ![](https://opencv.github.io/cvat/images/image167.jpg) | `Rectangle` | ==[Shape Mode](#Shape)==；==[Track Mode](#Track)==|

    ### 人工智能工具

    要使用檢測器進行註釋，請執行以下操作：
    1. 單擊**Magic wand** ![魔法棒](https://opencv.github.io/cvat/images/image189.jpg)，然後轉到**Detectors**選項卡。
    2. 從**模型**下拉列表中，選擇**Model**
    3. 從左側下拉列表中選擇 DL 模型標籤，從右側下拉列表中選擇任務的匹配標籤。
    ![](https://i.imgur.com/4DPPaJJ.png)
    4. 點擊**Annotate**

# 矩形標註
## Shape
在**Shape**模式下標註時可用的使用示例和基本操作。
使用示例：
- 為一組圖像創建新註釋。
- 添加/修改/刪除現有註釋的對象。
1. **您需要`Rectangle`在控件側邊欄上選擇：**
    ![](https://i.imgur.com/lTthKBt.png)

    **選擇正確的 Drawing Method 我們使用 ==2 Points==**
    ![](https://i.imgur.com/6FJiu0P.png)
2. **在中創建一個新註釋Shape mode：**

    Rectangle通過單擊創建一個單獨的Shape。
    ![](https://i.imgur.com/zyeoTcl.png)

    **選擇相反的點。您的第一個矩形已準備就緒！**
    ![](https://i.imgur.com/GUh0jGR.png)

    **可以使用鼠標調整矩形的邊界和位置。矩形的大小顯示在右上角，您可以通過單擊形狀的任意一點來查看它。您還可以使用或撤消您的操作`Ctrl+Z`並重做它們。`Shift+Ctrl+Z` 或 `Ctrl+Y`**

3. **您可以`Object card`在對象側邊欄中看到或通過右鍵單擊對象將其打開。您可以在詳細信息部分更改屬性。您可以通過單擊操作菜單按鈕執行基本操作或刪除對象。**
    ![](https://i.imgur.com/3Gx63Gt.png)

4. **下圖是一個帶有單獨形狀的完整註釋框架的示例。**
    ![](https://i.imgur.com/TQpK8mq.png)

## Track
**Track**模式標註時可用的使用示例和基本操作。

使用示例：
為一系列幀創建新註釋。
- 添加/修改/刪除現有註釋的對象。
- 編輯**Track**，將多個矩形合併為一個軌道。
1. 和`Shape mode`一樣，你需要`Rectangle`在側邊欄上選擇一個，在出現的表格中，選擇想要`Label`的和`Drawing method`。
    ![](https://i.imgur.com/jCnxMOk.png)

2. 為物體創建**Track**（以選中的汽車為例）：
    通過單擊創建一個**Rectangle** - **Track mode**
    ![](https://i.imgur.com/hmtBi5x.png)
    在Track mode矩形中將自動插值到下一幀。

    騎自行車的人在第 2270 幀開始移動。讓我們將幀標記為關鍵幀。
    您可以按下**K**或單擊**star**按鈕，請參見下面的屏幕截圖。
    ![](https://i.imgur.com/tLuSNEz.gif)


    如果對像開始改變它的位置，你需要修改它發生的矩形。無需更改每一幀上的矩形，只需更新幾個關鍵幀，它們之間的幀將自動插值。

    讓我們向前跳 30 幀並調整對象的邊界。請參見下面的示例：
    ![](https://i.imgur.com/RugWlf7.png)

3. 當被標註對象消失或變得太小時，您需要完成追踪。你要選擇**Outside Property**，捷徑**O**。
    ![](https://i.imgur.com/49owcnG.png)

4. 如果對像在幾幀中不可見然後再次出現，您可以使用該**Merge**功能將多個單獨的軌道合併為一個。
    ![](https://i.imgur.com/dZ9LYFi.png)

    為騎車人可見的時刻創建軌跡：
    ![](https://i.imgur.com/VaLY0bV.gif)


    單擊**Merge**按鈕或按鍵**M**，然後單擊第一條軌道的任意矩形和第二條軌道的任意矩形，依此類推：
    ![](https://i.imgur.com/RiXT5nX.png)

    單擊**Merge**按鈕或按下**M**以應用更改。
    ![](https://i.imgur.com/mk9DvBA.png)

    模式中最終帶註釋的幀序列**Interpolation**可能類似於下面的剪輯：
    ![](https://i.imgur.com/0THgf7S.gif)



''')