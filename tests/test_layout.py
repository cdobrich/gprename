import ast
from pathlib import Path


SOURCE = Path(__file__).resolve().parents[1] / "src" / "gprename"


def _layout_namespace():
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    names = {
        "INITIAL_TREE_WIDTH_PERCENT",
        "INITIAL_OPERATION_HEIGHT_PERCENT",
        "initial_pane_positions",
    }
    nodes = [
        node
        for node in tree.body
        if isinstance(node, (ast.Assign, ast.FunctionDef))
        and (
            any(
                isinstance(target, ast.Name) and target.id in names
                for target in getattr(node, "targets", [])
            )
            if isinstance(node, ast.Assign)
            else node.name in names
        )
    ]
    namespace = {}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(SOURCE), "exec"), namespace)
    return namespace


def test_initial_pane_percentages():
    ns = _layout_namespace()
    assert ns["INITIAL_TREE_WIDTH_PERCENT"] == 25
    assert ns["INITIAL_OPERATION_HEIGHT_PERCENT"] == 35


def test_initial_pane_positions_are_25_and_65_percent():
    ns = _layout_namespace()
    horizontal, vertical = ns["initial_pane_positions"](1200, 800)
    assert horizontal == 300
    assert vertical == 520


def test_initial_pane_positions_scale_with_window_size():
    ns = _layout_namespace()
    horizontal, vertical = ns["initial_pane_positions"](1600, 1000)
    assert horizontal == 400
    assert vertical == 650
