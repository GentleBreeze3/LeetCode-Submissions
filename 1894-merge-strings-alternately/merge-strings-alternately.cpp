class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result="";
        int count = 0;
        int minLength = min(word1.size(), word2.size());
        
        while (count < minLength) {
            result += word1[count];
            result += word2[count];
            count++;
        }
        
        result += word1.substr(count);
        result += word2.substr(count);
        
        return result;
    }
};