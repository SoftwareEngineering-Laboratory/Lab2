
# داک پروژه 

در این قسمت به مستندات پروژه می‌پردازیم.
## پکیج‌های پایتونی 
در این پروژه تنها یک پکیج shape قرار دارد که کد‌های مربوط به این آزمایش در آن قرار گرفته‌است.
### پکیج shape 
_**_این پکیج دارای دو فایل می باشد._**_

- فایل **shapes.py**:

در این فایل کلاس‌های مربوط به پروژه را پیاده‌سازی کرده‌ایم. 
کلاس Shape یک کلاس ابسترکت است که دو کلاس دیگر یعنی Rectangel و Square از آن ارث بری کرده‌اند و تابع compute_area را در خود overwrite کرده‌اند تا چند ریختی را در این ساختار فراهم آورند.

کلاس Rectangle یک کلاس concrete می‌باشد که دارای متد compute_area برای محاسبه مساحت خود است و چهار تابع دیگر نیز دارد که مربوط به set و get کردن طول و عرض مستطیل است.

کلاس Square نیز تنها دارای متد  computea_area می‌باشد که مساحت مربع مربوطه را محاسبه می‌کند.

در این ساختار همان طور که مشخص است چند ریختی برقرار است و کلاس‌های مختلف دیگر نیز می‌توانند با ارث بری از Shape و پیاده‌سازی متد compute_area به دسته‌های شکل اضافه شوند. به طوری که کلاینت اگر فقط به اینترفیس کلاس Shape دسترسی داشته باشد نیز می‌تواند نتایج مطلوب را در محاسبه مساحت بگیرد. البته پیش از‌ این‌ها یک پیکربند باید یک instance  از کلاس concrete مربوطه را در اختیار کلاینت قرار دهد.

اما در مورد set , get طول و عرض برای مستطیل چون یک چیز منحصر به فرد برای فقط مستطیل است و نمی‌توان آن را به مربع تعمیم داد ( به علت اینکه مربع نمی‌تواند طول و عرض متفاوت داشته باشد) داستان فرق دارد و کلاینت برای بهره‌بری از این متد‌ها باید به صورت مستقیم به کلاس Rectangle دسترسی داشته باشد زیرا اینترفیس کلاس Shape این متد‌ها را در خود ندارد.

- فایل **test.py**:

در این فایل تست‌های مربوط به کلاس‌های پیاده‌سازی شده در فایل shapes.py را نوشته‌ایم. به طور کلی دو دسته تست داریم.

1. تست‌های مربوط به مستطیل که در کلاس TestRectangle پیاده‌سازی شده اند و درکل سه تابع تست هستند. اولی مربوط به تست مساحت مستطیل، دومی مربوط به تست  set و get عرض مستطیل و سومی مربوط به تست  set و get طول مستطیل است.
2. تست‌های مربوط به مربع در کلاس TestSquare پیاده‌سازی شده اند. در کل یک تست برای مساحت مربع نوشته شده است، که تنها متد کلاس Square می‌باشد و این تست صحت مساحت محاسبه شده توسط متد compute_area در Square را می‌آزماید.

### اصول SOLID

- در این پروژه یکی از اصولی که کاملا مشهود است LSP می‌باشد به طوری که تمامی فرزندان کلاس Shape می‌توانند به جای Shape بنشینند. زیرا پیش‌شرط‌های بیش‌تر ندارند و همچنین پس‌شرط‌های بیشترمساوی با کلاس پدر را ارضا می‌کنند.
- اصل دیگری که در این پیاده سازی وچود دارد، اصل OCP می‌باشد به نوعی که اگر دقت کنید، برای افزودن یک شکل هندسی دیگر به پروژه، نیاز به تغییر کلاس‌های از قبل پیاده‌سازی شده وجود ندارد و فقط کافیست که کلاس شکل جدید را به کد اضافه کنیم. که این دقیقا همان اصل OCP است که در این مسئله با این نوع پیاده سازی ارضا شده است.
- اصل SRP را نیز می‌توان در این پیاده‌سازی مشاهده کرد. زیرا همانطور که این اصل می‌گوید، تمام کلاس‌ها فقط یک دلیل برای تغییر دارند، زیرا که هر کدام تنها با یک نوع کلاینت سر و کار دارند و وابستگی بین کلاس‌های concrete بسیار کم است. که به همین دلیل احتمال بروز تغییرات منتشر شونده بسیار کاهش پیدا می‌کند، و این یکی از مزیت‌های پیروی از اصل SRP است.

---

#           پرسش‌ها  
#### ۱. هر یک از پنج اصل SOLID را در دو الی سه خط توضیح دهید. 

- **SRP** : 

توضیح اصل

- **OCP** : 

توضیح اصل

- **LSP** :

توضیح اصل

- **ISP** :

توضیح اصل

- **DIP** :

توضیح اصل



#### ۲. اصول SOLID در کدام یک از گام‌های اصلی ایجاد نرم‌افزار (تحلیل نیازمندی‌ها، طراحی، پیاده‌سازی، تست و استقرار) استفاده می‌شوند؟ توضیح دهید.

- **تحلیل**:

 در فاز تحلیل، تمرکز شما بر استخراج نیازمندی‌ها و شناسایی عملکردهای کلیدی نرم‌افزار می‌باشد و اصول SOLID نقش پررنگی در تصمیمات فاز تحلیل ایفا نمی‌کنند اما اگرچه در این فاز اصول SOLID به صورت صریح به کار نخواهند رفت، اما اعمال این فاز به عنوان یک پایه برای انجام تصمیمات طراحی است که در فاز‌های بعد با اصول SOLID هماهنگ خواهند بود.

- **طراحی**:

اصول SOLID به شدت در فاز طراحی تاثیر گذار خواهند بود و به طور مستقیم در طراحی اعمال می‌شوند. از کشیدن دیاگرام کلاس طراحی گرفته تا نحوه ارتباط اشیا و کامپوننت‌ها با یکدیگر،‌اصول SOLID را می‌توان روی آن‌ها منعکس کرد تا بتوان از مزایای این اصول بهره برد.

- **پیاده‌سازی**:

در فاز پیاده‌سازی با توجه به زبان برنامه نویسی انتخاب شده، طراحی که در فاز قبلی انجام شده است را باید به صورت کد در بیاوریم. همانطور که در بخش طراحی گفتیم اصول SOLID در‌ آن‌جا باید تا حد زیادی رعایت شوند و در فاز پیاده‌سازی نیز آن اصول طراحی شده باید پیاده‌سازی شوند. در این جا ممکن است پیاده‌سازی اصول ذکر شده در زبان‌‌های برنامه نویسی مختلف، متفاوت از یکدیگر باشند که باید طبق idiom های زبان پیش برویم و پیاده‌سازی مطلوبی را ارائه دهیم.
- **آزمون**:

در این مرحله از ایجاد نرم‌افزار،‌اصول SOLID به طور غیر مستقیم روی آزمون پذیری کد ما تاثیر گذار خواهد بود. به این صورت که اگر در مراحل پیش به درستی از این اصول بهره برده باشیم، کدی که زده‌ایم ماژولار خواهد بود و همچنین قسمت‌های مختلف وابستگی کمی به یکدیگر دارند که این باعث می‌شود بتوانیم قسمت‌های مختلف کد را به صورت مستقل تست کنیم و unit-test را در کدمان داشته باشیم. رعایت اصول SOLID در نهایت به راحتی تست کردن کد منجر می‌شود که دستاورد خیلی مهمی است.

- **استقرار**:

این اصول در فاز اسقرار به صورت مستقیم تاثیری ندارند. در عوض اگر از این اصول در فاز‌های قبلی و در کل در طول فرآیند ایجاد نرم‌افزار به درستی استفاده کرده باشیم، محصولی که در حال آماده‌سازی و مستقرسازی آن هستیم، به مراتب قابل اطمینان‌تر است و همچنین بعد از مستقرسازی و در قسمت پشتیبانی نیز کارمان راحت‌تر می‌شود زیرا محصول تحویل داده شده، قابلیت نگهداری بسیار بالایی دارد.

در نهایت باید بگوییم که استفاده از اصول SOLID در ایجاد یک نرم‌افزار، به تولید یک محصول robust و maintainable منجر می‌شود.
####    ۳. در چرخه‌ی عمومی ایجاد نرم‌افزار، آزمون نرم‌افزار دیرتر از پیاده‌سازی نرم‌افزار انجام می‌شود، اما در روش TDD تست‌نویسی پیش از پیاده‌سازی شروع می‌شود. آیا این دو مورد با هم تناقضی دارند؟ توضیح دهید.

به طور ذاتی این دو روش با یکدیگر نتاقضی ندارند.
روش سنتی ایجاد نرم‌افزار بر روی انجام مراحل در یک ترتیب خاص تمرکز دارد درحالی که TDD روشی است که تست در آن پیش از پیاده‌سازی صورت می‌گیرد. در واقع اگر حتی از روش TDD استفاده کنیم، نرم‌افزار پس از مرحله پیاده‌سازی باز هم نیازمند تست می‌باشد، همان تست سنتی چرخه ایجاد نرم‌افزار که شامل 
integration testing, system testing, user acceptance testing
می‌شود.

پس به طور خلاصه، روش TDD یک نگاه مکمل و تکرارشونده است که تاکیدش بر روی نوشتن تست پیش از پیاده‌سازی می‌باشد که می‌تواند با روش سنتی ایجاد نرم‌افزار نیز ترکیب شود و یک نرم‌افزار با کیفیت خروجی دهد که تمامی نیازمندی‌ها را به خوبی پوشش داده‌است.

#### ۴. فرض کنید در آزمایش بالا نیازی به تغییر ابعاد مستطیل نداشتیم. آیا در این حالت می‌توانستیم مربع را از مستطیل به ارث ببریم؟ توضیح دهید.

با فرضیات بالا بله می‌شد. زیرا تنها متدی که باقی می‌ماند همان محاسبه مساحت بود.
همچنین اگر این ارث بری انجام می‌شد مشکلی در اصل LSP نیز پیش نمی‌آمد زیرا چون مربع نوعی از مستطیل است می‌توانست به جای کلاس پدر(مستطیل) بشیند و مشکلی هم پیش نیاید.

اما توجه کنید که این تنها زمانی است که متد دیگری اضافه نشود که فقط مربوط به مستطیل باشد و چنین چیزی برای مربع غیر قابل تعریف باشد. در این صورت مانند مثال این آزمایش (ست کردن طول و عرض) اصل LSP نقض می‌شد و مربع نمی‌توانست به جای مستطیل بشیند زیرا همچنین متدی برای مربع غیر قابل تعریف است و در ذات آن وجود ندارد.