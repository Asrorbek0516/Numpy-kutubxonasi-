# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rOmAmje1_Gu0aVPSwDE3zrgenw5XDUYE
"""

import pandas as pd
guruh=pd.DataFrame({
                    'Ism':[ 'Asrorbek' ,'Muhammadiyor','Imomali','Dilshod','Sarvar','Oybek','Ilhom','Humoyun','Alisher','Behruz','Sanjar' ],
                    'Familiya':[ 'Alimqulov','Tolibjonov','Nuriddinjonov','Ikromaliyev','Shakirjonov','Turanboyev','Abduhakimov','Hasanboyev','Erkinov','Joraboyev','Qosimaliyev'   ],
                    'Manzil':[ 'Namangan ','Bogdod','Quvasoy','Toshkent','Bogdod','Beshariq','Quvasoy','Andijon','Namangan','Namangan','Qoqon'  ],
                    'Tel raqam':[ '+998947961005','+998910080402','+998770200103','+998934456787','+998935678909','+998772345676','+998976785434','+998884566676','+998908909080','+998911213141','+998500052005'   ]
})
print(guruh)

guruh.to_excel('guruh.xlsx')

