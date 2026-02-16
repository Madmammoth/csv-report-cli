import pytest

from main import main


def test_main_average_gdp_success(tmp_path, capsys):
    csv_dir = tmp_path / "csv_files"
    csv_dir.mkdir()
    (csv_dir / "a.csv").write_text("country,year,gdp\nTest_country,2023,10\n")
    main(["--files", "a.csv", "--report", "average-gdp"], base_dir=csv_dir)
    out = capsys.readouterr().out
    assert "Test_country" in out


def test_main_missing_files(capsys):
    with pytest.raises(SystemExit):
        main(["--report", "average-gdp"])
    err = capsys.readouterr().err
    assert "--files" in err


def test_main_missing_report(capsys):
    with pytest.raises(SystemExit):
        main(["--files", "a.csv"])
    err = capsys.readouterr().err
    assert "--report" in err


def test_main_wrong_files(capsys):
    with pytest.raises(SystemExit):
        main(["--files", "wrong.csv", "--report", "average-gdp"])
    err = capsys.readouterr().err
    assert "unknown file name" in err


def test_main_wrong_report(capsys):
    with pytest.raises(SystemExit):
        main(["--files", "a.csv", "--report", "wrong"])
    err = capsys.readouterr().err
    assert "invalid choice" in err
