"""Export the current opportunity JSON schema for prompts and integrations."""

import json
from pathlib import Path

from reach_ai_schemas import OpportunityExtraction


def main() -> None:
    output = Path(__file__).resolve().parents[1] / "generated" / "opportunity-v1.schema.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(OpportunityExtraction.model_json_schema(), indent=2) + "\n",
        encoding="utf-8",
    )
    print(output)


if __name__ == "__main__":
    main()
