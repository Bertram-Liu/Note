"""
demo05_movie.py  电影推荐
"""
import json
import numpy as np

with open('../ml_data/ratings.json', 'r') as f:
    ratings = json.loads(f.read())
# 获取所有用户列表
users = list(ratings.keys())
# 存储用户与用户之间相似度信息的矩阵
scmat = []
for user1 in users:
	scrow = []   # 存储user1对所有用户的相似度得分
	for user2 in users:
		movies = set() # 存储两个人都看过的电影
		for movie in ratings[user1]:
			if movie in ratings[user2]:
				movies.add(movie)
		# 通过movies列表 计算两人的相似度得分
		if len(movies) == 0:
			score = 0
		else:  
		    # a:存储user1的电影评分  b:存储user2的电影评分
		    a, b = [], []
		    for movie in movies:
		    	a.append(ratings[user1][movie])
		    	b.append(ratings[user2][movie])
		    # 通过欧式距离得分算法计算相似度
		    a = np.array(a)
		    b = np.array(b)
		    score = np.corrcoef(a,b)[0,1]
			# score = 1 / (1+np.sqrt(((a-b)**2).sum()))
		scrow.append(score)
	scmat.append(scrow)

print(np.round(scmat, 2))

scmat = np.array(scmat)
users = np.array(users)
# 按照相似度从高到低排列每个用户的相似用户
for i, user in enumerate(users):
	sorted_indices=scmat[i].argsort()[::-1]
	# 除去自己，对相似用户排序  从大到小
	sorted_indices=sorted_indices[sorted_indices!=i]
	sim_users = users[sorted_indices]
	sim_scores = scmat[i, sorted_indices]
	# print(user, sim_users, sim_scores)
	# 相似度得分正相关的掩码
	positive_mask = sim_scores > 0
	sim_users = sim_users[positive_mask]
	# {'name1':[2.5, 3.0], 'name2':[1.0, 4.5]..}
	recom_movies = {}
	for i, sim_user in enumerate(sim_users):
		for movie, score in ratings[sim_user].items():
			# 若相似用户看过，但当前用户没看过
			if movie not in ratings[user].keys():
				if movie not in recom_movies:
					recom_movies[movie] = [score]
				else:
					recom_movies[movie].append(score)

	print(user)
	# 排序
	movie_list = sorted(recom_movies.items(), 
		key=lambda x: np.average(x[1]), 
		reverse=True)
	print(movie_list)
