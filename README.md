# matplotlib-extract
This package is useful to create dynamic presentations where elements of a plot appear one by one. To do so, the elements are exported to seperate files.

**Install with**

```
pip install matplotlib-extract
```

**Usage**

```python

import matplotlib.pyplot as plt
from matplotlib_extract import extract_elements

import numpy as np

x = np.linspace(0, 2*np.pi)
y1 = 2*x
y2 = 6 + 2*np.sin(x)

plt.plot(x, y1, label="line1")
plt.plot(x, y2, label="line2")
plt.legend()

extract_elements()

plt.show()
```

Running this script will create files for the lines, the axis and the legend.
