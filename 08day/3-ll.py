nclude<iostream>
#include<time.h>

using namespace std;

const int R = 0;//石头
const int P = 1;//布
const int S = 2;//剪刀

void win(int x)

    int irand = rand()%3;
    switch (irand)
    
    case 0:
        cout << "我出的是石头" << endl;
        break;
    case 1:
        cout << "我出的是布" << endl;
        break;
    case 2:
        cout << "我出的是剪刀" << endl;
        break;
    default:
        break;
    
    switch (irand - x)
    
    case 0:
        cout << "平局" << endl;
        break;
    case 1:
        cout << "你输了" << endl;
        break;
    case 2:
        cout << "你赢了" << endl;
        break;
    case -1:
        cout << "你赢了" << endl;
        break;
    case -2:
        cout << "你输了" << endl;
        break;
    default:
        break;
    


bool goon(char goon)

    cout << "三局到了,是否要继续?(Y 继续  N 结束)" << endl;
    cin >> goon;
    switch (goon)
    {
    case 'Y':
        return true;
        break;
    case 'y':
        return true;
        break;
    case 'N':
        return false;
        break;
    case 'n':
        return false;
        break;
    default:
        cout << "输入有误,请重新输入" << endl;
        ::goon(' ');
        break;
    


int main()

    srand((int)time(NULL));
    int n(3);
    while (n--)
    
        int m;
        cout << "请输入0-2(0代表石头,1代表布,2代表剪刀):" << endl;
        cin >> m;
        win(m);
        if (n == 0)
        {
            if (goon(m))
                n = 3;
        
    


