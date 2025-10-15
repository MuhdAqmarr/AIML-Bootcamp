import datetime
import inspect

dtclasses=inspect.getmembers(datetime, inspect.isclass)
print("All classes in datetime module: ")
for n, func in dtclasses:
    print(n, end=', ')

print("\n---Today---\n")
print(datetime.date.today())
print("\n---Current Date and Time---\n")
print(datetime.datetime.now().replace(microsecond=0))
print("\n---Current Time---\n")
print(datetime.datetime.now().time().replace(microsecond=0))

cttime=datetime.datetime.now().time()
formatedtime=datetime.datetime.now().strftime('%I:%M:%S %p')

print('Current time is:', cttime)
print('Formated time is:', formatedtime)