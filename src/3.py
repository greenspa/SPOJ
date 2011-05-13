#!/usr/bin/env python
# -*- coding: utf-8 -*-

numberOfCase = input(); #何組の数字が入ってくるのか
L=[] #入ってきた数字を入れるリスト

for i in range(numberOfCase):
	i = raw_input()
	L.append(i.split(" "))


def makeReverse(revNum):
	#裏向き数字にする
	trueNum = 0
	
	#扱いやすくするために、まずは文字列にする
	revNum = str(revNum)
	
	#下の桁から見ていく。
	#一番下の桁が0だったら、それが0でなくなるまで取り除く
	while(revNum[-1:] == '0'):
		revNum = revNum[:-1]
	
	#裏向きにしたあとの桁数(totalDigit)を求める
	totalDigit = len(revNum)
	
	#下の桁から順番にかけ算していく
	while(len(revNum) != 0):
		trueNum = trueNum + int(revNum[-1:])  * 10 ** (totalDigit - 1)
	
	return trueNum


for i in range(numberOfCase):
	revNumPairs = L[i]
	a = makeReverse(revNumPairs[0])
	b = makeReverse(revNumPairs[1])
	result = makeReverse( a + b )
