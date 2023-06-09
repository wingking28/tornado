# flake8: noqa
# Dummy source file to allow creation of the initial .po file in the
# same way as a real project.  I'm not entirely sure about the real
# workflow here, but this seems to work.
#
# 1) xgettext --language=Python --keyword=_:1,2 --keyword=pgettext:1c,2 --keyword=pgettext:1c,2,3 extract_me.py -o tornado_test.po
# 2) Edit tornado_test.po, setting CHARSET, Plural-Forms and setting msgstr
# 3) msgfmt tornado_test.po -o tornado_test.mo
# 4) Put the file in the proper location: $LANG/LC_MESSAGES

_("school")  # type: ignore[name-defined]
pgettext("law", "right")  # type: ignore[name-defined]
pgettext("good", "right")  # type: ignore[name-defined]
pgettext("organization", "club", "clubs", 1)  # type: ignore[name-defined]
pgettext("stick", "club", "clubs", 1)  # type: ignore[name-defined]
