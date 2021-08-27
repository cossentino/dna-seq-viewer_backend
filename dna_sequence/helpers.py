"""Helpers for Sequence views"""
from .models import SequenceFeature
import pdb

# Create Django API model of sequence feature from BioPython SeqFeature object


def create_feature(seq_feature, seq):
    """Factor out creation of new SequenceFeature instance"""

    pdb.set_trace()
    feature = SequenceFeature.new(
        start=int(seq_feature.location.start),
        end=int(seq_feature.location.end),
        feature_type=seq_feature.type,
        note=seq_feature.qualifiers.get('note', ""),
        db_xref=seq_feature.qualifiers.get(
            'db_xref', []),
        sequence=seq)
    try:
        feature.save()
    except Exception as e:
        print(e)
        return
