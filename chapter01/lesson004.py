s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
oneword_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

print({
    (w[:1] if (i+1) in oneword_list else w[:2]) : (i+1)
    for i, w in enumerate(s.replace(",", "").replace(".", "").split(" "))
})
