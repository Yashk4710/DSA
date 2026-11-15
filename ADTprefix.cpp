#include <iostream>
#include <cstring>
#include <cmath>
#include <cctype>
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

// Peek operation
char peek()
{
    if (top == NULL)
        return '\0';
    return top->data;
}

int precedence(char op)
{
    if (op == '^')
        return 3;
    if (op == '*' || op == '/')
        return 2;
    if (op == '+' || op == '-')
        return 1;
    return 0;
}

// Infix to Prefix
void infixToPrefix(char infix[], char prefix[])
{
    char rev[100], post[100];
    int n = strlen(infix);
    int j = 0;

    for (int i = n - 1; i >= 0; i--)
    {
        if (infix[i] == '(')
            rev[j++] = ')';
        else if (infix[i] == ')')
            rev[j++] = '(';
        else
            rev[j++] = infix[i];
    }
    rev[j] = '\0';

    j = 0;

    for (int i = 0; rev[i] != '\0'; i++)
    {
        char ch = rev[i];

        if (ch == ' ')
            continue;

        if (isalnum(ch))
            post[j++] = ch;
        else if (ch == '(')
            push(ch);
        else if (ch == ')')
        {
            while (top != NULL && peek() != '(')
                post[j++] = pop();

            if (top != NULL)
                pop();
        }
        else
        {
            while (top != NULL && peek() != '(' &&
                   precedence(peek()) > precedence(ch))
                post[j++] = pop();

            push(ch);
        }
    }

    while (top != NULL)
        post[j++] = pop();

    post[j] = '\0';

    for (int i = 0; i < j; i++)
        prefix[i] = post[j - i - 1];

    prefix[j] = '\0';
}

// Evaluate Prefix
int evaluatePrefix(char prefix[])
{
    int stack[100], t = -1;

    for (int i = strlen(prefix) - 1; i >= 0; i--)
    {
        char ch = prefix[i];

        if (isdigit(ch))
            stack[++t] = ch - '0';
        else
        {
            int a = stack[t--];
            int b = stack[t--];
            int result = 0;

            switch (ch)
            {
            case '+': result = a + b; break;
            case '-': result = a - b; break;
            case '*': result = a * b; break;
            case '/': result = a / b; break;
            case '^': result = pow(a, b); break;
            }

            stack[++t] = result;
        }
    }

    return stack[t];
}

int main()
{
    char infix[100], prefix[100];

    cout << "Enter infix expression: ";
    cin.getline(infix, 100);

    infixToPrefix(infix, prefix);

    cout << "Prefix Expression: " << prefix << endl;

    cout << "Evaluation: " << evaluatePrefix(prefix) << endl;

    return 0;
}