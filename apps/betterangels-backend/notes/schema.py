from typing import List, Optional

import strawberry
from strawberry.types import Info
from strawberry_django.auth.utils import get_current_user

from .models import Note
from .types import CreateNoteInput, NoteType, UpdateNoteInput


@strawberry.type
class Query:
    @strawberry.field
    def notes(self, info: Info) -> List[NoteType]:
        user = get_current_user(info)
        if user.is_authenticated:
            # Need to figure out types here
            return list(Note.objects.filter(created_by=user))  # type: ignore
        else:
            return []

    @strawberry.field
    def note(self, id: strawberry.ID, info: Info) -> Optional[NoteType]:
        user = get_current_user(info)
        if user.is_authenticated:
            # Need to figure out types here
            return Note.objects.get(id=id)  # type: ignore
        else:
            return None


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_note(self, info: Info, input: CreateNoteInput) -> Optional[NoteType]:
        user = get_current_user(info)
        if user.is_authenticated:
            # Need to figure out types here
            return Note.objects.create(
                created_by=user, title=input.title, body=input.body  # type: ignore
            )
        else:
            return None

    @strawberry.mutation
    def update_note(self, info: Info, input: UpdateNoteInput) -> Optional[NoteType]:
        user = get_current_user(info)
        if user.is_authenticated:
            # Need to figure out types here
            note = Note.objects.get(id=input.id)
            note.title = input.title
            note.body = input.body
            note.save()
            return note  # type: ignore
        else:
            return None

    @strawberry.mutation
    def delete_note(
        self,
        info: Info,
        id: strawberry.ID,
    ) -> bool:
        user = get_current_user(info)
        if user.is_authenticated:
            # Need to figure out types here
            note = Note.objects.get(id=id)
            note.delete()
            return True
        else:
            return False