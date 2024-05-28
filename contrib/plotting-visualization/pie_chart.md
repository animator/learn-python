# Pie chart
* It is a circle chart which is divided into slices to illustrate numerical portortions.
* With PyPlot it can created using Pie() function.
* Pie() function can only plot single type of data range only.

`Labels` is used to label Slices of pie
example:

    import matplotlib.pyplot as plt
    contri=[17,8.8,12.75,14]
    houses=["vidya","riya","sneha","narmita"]
    plt.pie(contri,labels=houses)
    plt.show()

* `autopct` is used to add formatted slice percentages to the pie chart.

  * `autopct  string format`   
**"%[flags][width][.precision]type"**



  * % symbol signifies that it is special string which will determine the format of the values to be displayed.
  * width determines the total number of characters to be displayed.
  * If the value displayed has lesser number of digits than the width specified then the vlaue is padded as per the fag specified.
  * precision determines the number of decimal places to be displayed.
  * type determines the type of the value to be displayed.
  * %%(two percentage signs) are used to print a % sign.
  * example:

  1.) Format String: "%05i%%"
  
  description:
  
  flag=0
  width =5 , type =integer type
  
  value=123

  printed value=00123 %
  (output is printed as 2 leading zeroes)

  2.) Format String: "%7.2f"
  
  description:
  
  width = 6 , type =float type
  
  value=12.567
  
  printed value=_12.57
  (output is printed as 1 leading blanks)


* `colors` is used to change the color of the slices.
eg:
```
colr = ['red', 'yellow', 'green', 'blue']

```
* `explode` is used to change the position of the slices.
    * It is used when we want to emphasize on one or more slices.
    * It makes slices pulled out by given distance.
    eg:

    ```
    expl=[0,0,0.3,0]
    # it makes third slice exploded with a distace of 0.3 units
    ```


* `shadow` is used to add shadow to the pie chart.
   * it takes boolean argument (i.e True ,False)

* `startangle` is used to change the starting angle of the pie chart.
* `wedgeprops` is used to change the properties of the wedges.
example:
```
wedge_properties = {'edgecolor': 'black','linewidth': 2,'linestyle': 'dashed','alpha': 0.7}   
```
* `textprops` is used to change the properties of the text.

  * fontsize: Sets the size of the font.
  * color: Specifies the color of the text. Accepts any valid color value in Matplotlib.
  * fontweight: Sets the weight of the font (e.g., 'normal', 'bold', 'heavy', 'light', etc.).
  * fontstyle: Defines the style of the font (e.g., 'normal', 'italic', 'oblique').
  * family: Sets the font family (e.g., 'serif', 'sans-serif', 'monospace').

```
text_properties = {'fontsize': 14,'color': 'green','fontweight': 'bold','fontstyle': 'italic','family': 'serif'}
```

* `labeldistance` is used to change the distance of the labels from the pie chart.
example:
  * labeldistance=1.0 places the labels exactly on the boundary of the pie.
  * labeldistance=1.2 places the labels slightly outside the boundary.
  * labeldistance=0.8 places the labels inside the boundary.



eg:


```
import matplotlib.pyplot as plt
contri=[17,8.8,12.75,14]
colr = ['red', 'yellow', 'green', 'blue']
houses=["vidya","riya","sneha","narmita"]
expl=[0,0,0.2,0]
wedge_properties = {'edgecolor': 'black','linewidth': 2,'linestyle': 'dashed','alpha': 0.7}
text_properties = {'fontsize': 14,'color': 'green','fontweight': 'bold','fontstyle': 'italic','family': 'serif'}

plt.pie(contri,labels=houses,colors=colr = ['red', 'yellow', 'green', 'blue'] , explode=expl,wedgeprops=wedge_properties ,shadow =True,
startangle=45 , textprops=text_properties,labeldistance=1.2 , autopct='%1.1f%%)
plt.show()
```

![example pie graph (output)](images/pie-chart.png)