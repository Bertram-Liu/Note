"""
demo05_gridsearch.py  网格搜索
"""
import numpy as np
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as mp

data = np.loadtxt('../ml_data/multiple2.txt', 
	delimiter=',', dtype='f8')
x = data[:, :-1]
y = data[:, -1]
# 选择svm做分类
train_x, test_x, train_y, test_y = \
    ms.train_test_split(x, y, test_size=0.25, 
    	random_state=5)
model = svm.SVC(probability=True)
# 根据网格搜索选择最优模型
params = [{'kernel':['linear'],'C':[1, 10, 100, 1000]},
    {'kernel':['poly'], 'C':[1], 'degree':[2, 3]}, 
    {'kernel':['rbf'], 'C':[1,10,100,1000], 
     'gamma':[1, 0.1, 0.01, 0.001]}]
model = ms.GridSearchCV(model, params, cv=5)
model.fit(train_x, train_y)

print(model.best_params_)
print(model.best_score_)
print(model.best_estimator_)

# 输出每个超参数组合信息及其得分
for param, score in zip(
	model.cv_results_['params'], 
	model.cv_results_['mean_test_score']):
	print(param, '->', score)


pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y, pred_test_y))

# 新增样本
prob_x = np.array([
    [2, 1.5],
    [8, 9],
    [4.8, 5.2],
    [4, 4],
    [2.5, 7],
    [7.6, 2],
    [5.4, 5.9]])
pred_prob_y = model.predict(prob_x)
probs = model.predict_proba(prob_x)
print(probs)


# 绘制分类边界线
n = 500
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
grid_x = np.meshgrid(np.linspace(l, r, n),
                     np.linspace(b, t, n))
flat_x = np.column_stack((grid_x[0].ravel(), grid_x[1].ravel()))    
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)

mp.figure('Probability', facecolor='lightgray')
mp.title('Probability', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y,
	cmap='gray')
mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y, cmap='brg', s=80)
mp.scatter(prob_x[:,0], prob_x[:,1], c=pred_prob_y,
	cmap='jet_r', s=80, marker='D')
for i in range(len(probs)):
    mp.annotate(
        '{}% {}%'.format(
            round(probs[i, 0] * 100, 2),
            round(probs[i, 1] * 100, 2)),
        xy=(prob_x[i, 0], prob_x[i, 1]),
        xytext=(12, -12),
        textcoords='offset points',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=9,
        bbox={'boxstyle': 'round,pad=0.6',
              'fc': 'orange', 'alpha': 0.8})
mp.show()