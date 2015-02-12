commit 06decf7f9c69239b4b264a299874ea6031e874d0
Author: Wilbert Ho <wilbert.ho@gmail.com>
Date:   Mon Feb 23 16:48:59 2015 +1300

    [valid parentheses] (python) Add test module.

diff --git a/easy/valid_parentheses/py/tests/test_validparentheses.py b/easy/valid_parentheses/py/tests/test_validparentheses.py
new file mode 100644
index 0000000..259bd42
--- /dev/null
+++ b/easy/valid_parentheses/py/tests/test_validparentheses.py
@@ -0,0 +1,11 @@
+from nose.tools import eq_
+from validparentheses import Solution
+
+
+def test_validparentheses():
+    s = Solution()
+    eq_(s.isValid('({[]})'), True)
+    eq_(s.isValid('()[]{}'), True)
+    eq_(s.isValid('([)]'), False)
+    eq_(s.isValid('([{}]'), False)
+    eq_(s.isValid('(()[]{})'), True)
