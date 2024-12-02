from marshmallow import Schema, fields

class CombatSchema(Schema):
    pkm1 = fields.String(required=True)
    pkm2 = fields.String(required=True)
