# Skopiowane dane z przeglądarki
crash_history = ['x1.25', 'x1.56', 'x1.10', 'x1.11', 'x8.68', 'x2.64', 'x1.25', 'x2.33', 'x2.75', 'x1.34', 'x11.82', 'x10.27', 'x5.67', 'x1.63', 'x11.92', 'x2.76', 'x2.23', 'x2.94', 'x1.37', 'x7.50', 'x6.47', 'x1.65', 'x23.97', 'x1.16', 'x1.21']

crash_history_floats = [float(x[1:]) for x in crash_history]
print(crash_history_floats)
