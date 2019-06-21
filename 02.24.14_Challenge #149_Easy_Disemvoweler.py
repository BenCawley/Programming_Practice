def setup():
    examples = {
        0 : 'all those who believe in psychokinesis raise my hand',
        1 : 'did you hear about the excellent farmer who was outstanding in his field'
    }

    offenders = ('a','e','i','o','u',' ')

    return [examples, offenders]

def Disemvoweler():
    examples, offenders = setup()[0], setup()[1]
    output = ['', '']
    rejected = ['', '']
    for v in examples:
        for l in examples[v]:
            if l in offenders:
               rejected[v] += l
            else:
                output[v] += l
    return output, rejected

print (Disemvoweler())