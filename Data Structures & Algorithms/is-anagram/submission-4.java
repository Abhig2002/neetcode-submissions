class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }else{
            int[] tarr = new int[26];
            int[] sarr = new int[26];

            for (int i = 0; i < s.length(); i++){
                tarr[t.charAt(i) - 'a']++;
                sarr[s.charAt(i) - 'a']++;
            }

            for (int i = 0; i < sarr.length; i++){
                if(sarr[i] != tarr[i]){
                    return false;
                }
            }

            return true;


        }
    }
}