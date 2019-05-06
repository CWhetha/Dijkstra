#include <string>
#include "unionfind.h"


treenode::treenode(int value) {
	val = value;
	parent = NULL;
}
bool treenode::isroot() {
	if (parent == NULL) {
		return true;
	}
	else {
		return false;
	}
}
void treenode::setvalue(int i) {
	val = i;
}
int treenode::getvalue() {
	return val;
}
void treenode::setparent(treenode *p) {
	parent = p;
}
treenode treenode::getparent() {
	return *parent;
}
void treenode::setchild(treenode t) {
	children.push_back(t);
}
std::vector<treenode> treenode::getchildren() {
	return children;
}

void UnionFind::uandf(int n) {
}
void UnionFind::makeSet(int i) {
	if (end == 0) {
		list.push_back(treenode(i));
	}
}
void UnionFind::unionSets(int i, int j) {
	treenode *nodei = NULL, *nodej = NULL;
	if (end == 0) {
		for (auto x = list.begin(); x != list.end(); x++) {
			if (findSet(i) != findSet(j) && x->getvalue()==findSet(i)) {
				nodei = &(getnode(&(*x),i));
				int coun = 0;
				for (auto y = &list.begin(); y != &list.end(); y++) {
					if ((y[0])->getvalue()!= nodei->getvalue()&& (y[0])->getvalue()==j) {
						nodei->setchild(*(y[0]));
						(y[0])->setparent(nodei);
						list.erase(list.begin() + coun);
						x = list.begin();
						y = &list.begin();
						coun = 0;
					}	
					coun++;
				}
			}
		}
	}

}
treenode UnionFind::getnode(treenode *x, int i) {
	std::vector<treenode> z = (*x).getchildren();
	for (auto y = z.begin(); y != z.end(); y++) {
		if (y->getvalue() == i) {
			return *y;
		}
		else if (y->getchildren().size() != 0) {
			getnode(&(*y), i);
		}
	}
	if (x->getvalue() == i) {
		return *x;
	}
	return NULL;
}
int UnionFind::findSet(int i) {
	treenode *node = NULL;
	for (auto x = list.begin(); x != list.end(); x++) {
		if (find(&(*x),i) == i) {
			node = &(*x);
			while (!node->isroot()) {
				node = &(node->getparent());
			}
			return node->getvalue();
		}
	}
	if (node == NULL){
		return -72;
	}
	
}
int UnionFind::find(treenode *x, int i) {
	std::vector<treenode> z = (*x).getchildren();
	for (auto y = z.begin(); y != z.end(); y++) {
			if (y->getvalue() == i) {
				return y->getvalue();
			}
			else if (y->getchildren().size() != 0) {
				find(&(*y), i); 
			}
	}
	if (x->getvalue() == i) {
		return x->getvalue();
	}
	return -72;
}
int UnionFind::finalSets() {
	count = 0;
	end = 1;

	for (auto x = list.begin(); x != list.end(); x++) {
		(*x).setvalue(count);
		count++;
	}
	return list.size();
}
