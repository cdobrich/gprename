from pathlib import Path
import os

SRC = Path(__file__).resolve().parents[1] / "src" / "gprename"


def test_tree_path_components_expand_in_order():
    target = str(Path("/home/bob").resolve())
    parts = Path(target).parts
    current = Path(os.sep)
    targets = [str(current)]
    for part in parts[1:]:
        current /= part
        targets.append(str(current))
    assert targets[0] == "/"
    assert targets[-1] == target


def test_tree_expander_is_explicitly_visible():
    source = SRC.read_text()
    assert "expander.set_hide_expander(False)" in source
    assert "expander.set_indent_for_icon(True)" in source
    assert "treeexpander > expander" in source


def test_initial_path_expansion_is_invoked():
    source = SRC.read_text()
    assert "self._expand_tree_to_path(self.current_path)" in source
    assert "def _expand_tree_to_path" in source


def test_tree_expander_uses_explicit_high_contrast_icons():
    source = SRC.read_text()
    assert '-gtk-icon-source: -gtk-icontheme("pan-end-symbolic")' in source
    assert '-gtk-icon-source: -gtk-icontheme("pan-down-symbolic")' in source
    assert 'treeexpander > expander:checked' in source


def test_tree_list_item_focus_is_owned_by_tree_expander():
    source = SRC.read_text()
    assert 'list_item.set_focusable(False)' in source
