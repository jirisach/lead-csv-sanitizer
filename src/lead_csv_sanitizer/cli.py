from pathlib import Path
import time
import typer

from lead_csv_sanitizer.loader import load_csv
from lead_csv_sanitizer.column_mapper import map_columns
from lead_csv_sanitizer.cleaner import clean_dataframe
from lead_csv_sanitizer.validators import validate_dataframe
from lead_csv_sanitizer.dedupe import detect_duplicates
from lead_csv_sanitizer.report import enrich_with_issue_flags
from lead_csv_sanitizer.writer import write_outputs

app = typer.Typer(help="Lead CSV Sanitizer")


@app.command()
def run(
    input_file: Path,
    country: str = "CZ",
    output_dir: Path = Path("output")
):
    """
    Sanitize lead CSV before CRM import.
    """

    start_time = time.perf_counter()

    output_dir.mkdir(exist_ok=True)

    df = load_csv(input_file)
    df = map_columns(df)
    df = clean_dataframe(df)
    df = validate_dataframe(df, default_country=country)
    df = detect_duplicates(df)
    df = enrich_with_issue_flags(df)

    report = write_outputs(df, output_dir)

    elapsed = time.perf_counter() - start_time
    rows_per_second = len(df) / elapsed if elapsed > 0 else 0

    typer.echo("Lead CSV Sanitizer")
    typer.echo(f"Input file: {input_file}")
    typer.echo(f"Country: {country}")
    typer.echo(f"Output directory: {output_dir}")
    typer.echo(f"Rows loaded: {len(df)}")
    typer.echo(f"Columns detected: {', '.join(df.columns)}")
    typer.echo(f"Valid emails: {report['valid_emails']}/{len(df)}")
    typer.echo(f"Valid phones: {report['valid_phones']}/{len(df)}")
    typer.echo(f"Duplicates detected: {report['duplicates']}")
    typer.echo(f"Missing first_name: {report['missing_first_name']}")
    typer.echo(f"Missing last_name: {report['missing_last_name']}")
    typer.echo(f"Missing email: {report['missing_email']}")
    typer.echo(f"Missing phone: {report['missing_phone']}")
    typer.echo(f"Missing company: {report['missing_company']}")
    typer.echo(f"Data health score: {report['data_health_score']}%")
    typer.echo(f"Cleaned rows: {report['cleaned_rows']}")
    typer.echo(f"Rejected rows: {report['rejected_rows']}")
    typer.echo(f"Processing time: {elapsed:.2f}s")
    typer.echo(f"Processing speed: {rows_per_second:.2f} rows/s")
    typer.echo("Files written:")
    typer.echo(f" - {report['output_files']['cleaned_csv']}")
    typer.echo(f" - {report['output_files']['crm_import_ready']}")
    typer.echo(f" - {report['output_files']['rejected_csv']}")
    typer.echo(f" - {report['output_files']['report_json']}")
    typer.echo("Sanitization complete")


if __name__ == "__main__":
    app()