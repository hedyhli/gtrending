import ast

import pytest


def test_version(script_runner):
    return_val = script_runner.run("gtrending", "--version")
    assert return_val.success
    assert return_val.stdout == "gtrending 0.3.0\n"
    assert return_val.stderr == ""


def test_help(script_runner):
    return_val = script_runner.run("gtrending", "--help")
    assert return_val.success
    assert "Fetch trending repositories/developers on github" in return_val.stdout
    assert return_val.stderr == ""


def test_repo_fail(script_runner):
    return_val = script_runner.run("gtrending", "repo")
    assert not return_val.success
    assert (
        "gtrending repo: error: the following arguments are required: language"
        in return_val.stderr
    )
    assert return_val.stdout == ""


def test_developer_fail(script_runner):
    return_val = script_runner.run("gtrending", "developer")
    assert not return_val.success
    assert (
        "gtrending developer: error: the following arguments are required: language"
        in return_val.stderr
    )
    assert return_val.stdout == ""


def test_repo_success(script_runner):
    return_val = script_runner.run("gtrending", "repo", "python")
    assert return_val.success
    assert return_val.stdout
    assert return_val.stderr == ""


def test_developer_success(script_runner):
    return_val = script_runner.run("gtrending", "developer", "python")
    assert return_val.success
    assert return_val.stdout
    assert return_val.stderr == ""
