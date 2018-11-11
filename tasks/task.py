from fabric import task, Connection

c = Connection()

@task
def test(c):
    print(c)
    result = c.local('dirs')
    print(result)