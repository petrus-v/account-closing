from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_columns(
        env.cr,
        {
            "account_cutoff_line": [
                ("parent_id", "cutoff_id"),
            ],
            "account_cutoff_tax_line": [
                ("parent_id", "cutoff_line_id"),
            ],
        },
    )
