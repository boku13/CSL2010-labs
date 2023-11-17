#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

// calculaing lexicographical value
int lex_order(string s1, string s2)
{
    int l1 = s1.length();
    int l2 = s2.length();
    for (int i = 0; (i < l1) && (i < l2); i++)
    {
        if (int(s1[i]) == int(s2[i]))
        {
            continue;
        }
        else if (int(s1[i]) < int(s2[i]))
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    if (l1 == l2)
    {
        return -1;
    }
    else if (l1 < l2)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

class HybridNode
{
public:
    string key;
    string element;
    HybridNode *parent;
    HybridNode *left_child;
    HybridNode *right_child;
    HybridNode *next_node;
    int word_occurances = 1;
    HybridNode(string key_val, string element_val) : key(key_val), element(element_val), parent(nullptr), left_child(nullptr), right_child(nullptr), next_node(nullptr) {}
};

class RedBlackTree
{
private:
    HybridNode *root = 0;

public:
    RedBlackTree() : root(nullptr) {}

    HybridNode *getRoot()
    {
        return root;
    }

    void setRoot(HybridNode *node)
    {
        root = node;
    }

    HybridNode *insert(string key, string element)
    {
        HybridNode *curr = root;
        if (curr == 0)
        {
            HybridNode *new_node = new HybridNode(key, element);
            new_node->parent = 0;
            root = new_node;
            return new_node;
        }
        HybridNode *prev = 0;
        while (curr != 0)
        {
            int x = lex_order(key, curr->key);
            if (x == -1)
            {
                HybridNode *temp = curr;
                HybridNode *prev_temp = curr;
                while (temp != 0)
                {
                    if (temp->element == element)
                    {
                        temp->word_occurances = temp->word_occurances + 1;
                        return temp;
                    }
                    prev_temp = temp;
                    temp = temp->next_node;
                }
                if (temp == 0)
                {
                    HybridNode *new_node = new HybridNode(key, element);
                    prev_temp->next_node = new_node;
                    new_node->parent = prev_temp;
                    return temp;
                }
            }
            else if (x == 1)
            {
                prev = curr;
                curr = curr->left_child;
            }
            else
            {
                prev = curr;
                curr = curr->right_child;
            }
        }
        if (curr == 0)
        {
            HybridNode *new_node = new HybridNode(key, element);
            int x = lex_order(key, prev->key);
            if (x == 1)
            {
                prev->left_child = new_node;
                new_node->parent = prev;
            }
            else
            {
                prev->right_child = new_node;
                new_node->parent = prev;
            }
            return new_node;
        }
    }

    void deletDeepest(HybridNode *root, HybridNode *d_node)
    {
        queue<HybridNode *> q;
        q.push(root);

        // Do level order traversal until last node
        HybridNode *temp;
        while (!q.empty())
        {
            temp = q.front();
            q.pop();
            if (temp == d_node)
            {
                temp = NULL;
                delete (d_node);
                return;
            }
            if (temp->right_child)
            {
                if (temp->right_child == d_node)
                {
                    temp->right_child = NULL;
                    delete (d_node);
                    return;
                }
                else
                    q.push(temp->right_child);
            }

            if (temp->left_child)
            {
                if (temp->left_child == d_node)
                {
                    temp->left_child = NULL;
                    delete (d_node);
                    return;
                }
                else
                    q.push(temp->left_child);
            }
        }
    }

    /* function to delete element in binary tree */
    bool deletion(HybridNode *root, string key)
    {
        if (root == NULL)
            return NULL;

        if (root->left_child == NULL && root->right_child == NULL)
        {
            if (root->key == key)
            {
                this->setRoot(0);
                return true;
            }
            else
            {
                return false;
            }
        }

        queue<HybridNode *> q;
        q.push(root);

        HybridNode *temp;
        HybridNode *key_node = NULL;

        // Do level order traversal to find deepest
        // node(temp) and node to be deleted (key_node)
        while (!q.empty())
        {
            temp = q.front();
            q.pop();

            if (temp->key == key)
                key_node = temp;

            if (temp->left_child)
                q.push(temp->left_child);

            if (temp->right_child)
                q.push(temp->right_child);
        }

        if (key_node != NULL)
        {
            string x = temp->key;
            deletDeepest(root, temp);
            key_node->key = x;
        }
        return true;
    }

    bool deleteNode(string key)
    {
        return deletion(this->getRoot(), key);
    }

    void traverseUp(HybridNode *node)
    {
        // Traverse up the tree from the given node to the root
    }

    void traverseDown(HybridNode *node, string bit_sequence)
    {
        // Traverse down the tree based on the bit sequence
    }

    void solve_preOrderTraversal(HybridNode *root, int &depth, int curr_depth, vector<string> &ans)
    {
        if (root == 0)
        {
            return;
        }
        if (curr_depth >= depth)
        {
            ans.push_back(root->key);
        }
        solve_preOrderTraversal(root->left_child, depth, curr_depth + 1, ans);
        solve_preOrderTraversal(root->right_child, depth, curr_depth + 1, ans);
        return;
    }

    vector<string> preOrderTraversal(HybridNode *node, int depth)
    {
        vector<string> ans;
        solve_preOrderTraversal(root, depth, 0, ans);
        vector<string> ans_2 = {};
        int i = 0;
        for (; i < ans.size(); i++)
        {
            if (ans[i] == node->key)
            {
                break;
            }
        }
        for (; i < ans.size(); i++)
        {
            ans_2.push_back(ans[i]);
        }
        return ans_2;
    }
    HybridNode *search(string key)
    {
        HybridNode *curr = root;
        while (curr != 0)
        {
            int x = lex_order(key, curr->key);
            if (x == -1)
            {
                return curr;
            }
            else if (x == 1)
            {
                curr = curr->left_child;
            }
            else
            {
                curr = curr->right_child;
            }
        }
        return 0;
    }

    int blackheight(HybridNode *node)
    {
        // Implement blackheight
        // vector <string> s = this->preOrderTraversal(this->getRoot(),0);

        int c = 0;
        HybridNode *curr = root;

        while (curr != node)
        {
            if (curr->key < node->key)
            {
                curr = curr->right_child;
            }
            else if (curr->key > node->key)
            {
                curr = curr->left_child;
            }
            c++;
        }

        vector<string> v = this->preOrderTraversal(node, 0);
        int n = v.size();

        return ceil(log2(n) - c / 2);
    }
};

class IndexEntry
{
private:
    string word;
    vector<pair<string, int>> chapter_word_counts; // List of (chapter, word_count) tuples

public:
    IndexEntry(string word_val) : word(word_val) {}

    void setWord(string word_val)
    {
        word = word_val;
    }

    string getWord()
    {
        return word;
    }

    void setChapterWordCounts(vector<pair<string, int>> chapter_word_counts_val)
    {
        chapter_word_counts = chapter_word_counts_val;
    }

    vector<pair<string, int>> getChapterWordCounts()
    {
        return chapter_word_counts;
    }

    void addOccurrence(string chapter, int word_count)
    {
        // Add a chapter's word count for this word
    }

    string toString()
    {
        // Return a string representation of the IndexEntry
        // Modify the implementation as needed for specific use cases
        return "";
    }
};

class Lexicon
{
private:
    RedBlackTree red_black_tree;

public:
    Lexicon() {}

    void setRedBlackTree(RedBlackTree tree)
    {
        red_black_tree = tree;
    }

    RedBlackTree getRedBlackTree()
    {
        return red_black_tree;
    }

    void solve_pruneRedBlackTree(HybridNode *root)
    {
        if (root == 0)
        {
            return;
        }
        solve_pruneRedBlackTree(root->left_child);
        solve_pruneRedBlackTree(root->right_child);
        HybridNode *temp = root;
        int c = 0;
        while (temp != 0)
        {
            temp = temp->next_node;
            c++;
        }
        if (c == 3)
        {
            red_black_tree.deleteNode(root->key);
        }
    }

    void pruneRedBlackTree()
    {
        solve_pruneRedBlackTree(red_black_tree.getRoot());
    }

    void readChapter(string chapter_name, vector<string> words)
    {
        // Process words from a chapter and update the Red-Black Tree
        for (int i = 0; i < words.size(); i++)
        {
            red_black_tree.insert(words[i], chapter_name);
        }
        pruneRedBlackTree();
    }

    void solve_buildIndex(HybridNode *root, vector<IndexEntry> &ans)
    {
        if (root == 0)
        {
            return;
        }
        solve_buildIndex(root->left_child, ans);
        IndexEntry i(root->key);
        HybridNode *temp = root;
        vector<pair<string, int>> v;
        while (temp != 0)
        {
            pair<string, int> p(temp->element, temp->word_occurances);
            v.push_back(p);
            temp = temp->next_node;
        }
        i.setChapterWordCounts(v);
        ans.push_back(i);
        solve_buildIndex(root->right_child, ans);
    }
    vector<IndexEntry> buildIndex()
    {
        vector<IndexEntry> ans;
        solve_buildIndex(red_black_tree.getRoot(), ans);
        return ans;
    }
};