from matplotlib import pyplot as plt

scores = []
with open('./scores/dynamic_alpha2.txt','r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        scores.append(float(line))


loss = scores
# epochs = [ i * 1000 for i in range(1, len(loss) + 1) ]
epochs = range(1, len(loss)*1000 + 1, 1000)
plt.plot(epochs, loss, 'y', label='mean score')
plt.xlabel('Episodes')
plt.ylabel('Score')
plt.legend()
plt.show()