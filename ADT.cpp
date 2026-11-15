#include <iostream>
#include <cstring>
using namespace std;

struct Node
{
    char data;
    Node* next;
};

Node* top = NULL;

// Push operation
void push(char x)
{
    Node* newNode = new Node;
    newNode->data = x;
    newNode->next = top;
    top = newNode;
}

// Pop operation
char pop()
{
    if (top == NULL)
        return '\0';

    Node* temp = top;
    char x = temp->data;
    top = top->next;
    delete temp;
    return x;
}

// Check top element
char peek()
{
    if (top == NULL)
        return '\0';
    return top->data;
}

// Check operator precedence
int precedence(char op)
{
    if (op == '^')
        return 3;
    else if (op == '*' || op == '/')
        return 2;
    else if (op == '+' || op == '-')
        return 1;
    return 0;
}

// Infix to Postfix conversion
void infixToPostfix(char infix[])
{
    char postfix[100];
    int j = 0;

    for (int i = 0; infix[i] != '\0'; i++)
    {
        char ch = infix[i];

        if (ch == ' ')
            continue;

        if ((ch >= 'A' && ch <= 'Z') ||
            (ch >= 'a' && ch <= 'z') ||
            (ch >= '0' && ch <= '9'))
        {
            postfix[j++] = ch;
        }
        else if (ch == '(')
        {
            push(ch);
        }
        else if (ch == ')')
        {
            while (top != NULL && peek() != '(')
                postfix[j++] = pop();

            if (top != NULL)
                pop();
        }
        else
        {
            while (top != NULL && peek() != '(' &&
                   precedence(peek()) >= precedence(ch))
            {
                postfix[j++] = pop();
            }

            push(ch);
        }
    }

    while (top != NULL)
        postfix[j++] = pop();

    postfix[j] = '\0';

    cout << "Postfix Expression: " << postfix << endl;
}

int main()
{
    char infix[100];

    cout << "Enter infix expression: ";
    cin.getline(infix, 100);

    infixToPostfix(infix);

    return 0;
}