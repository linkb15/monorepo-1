import { InfoIcon } from '@monorepo/expo/shared/icons';
import { Colors, Spacings } from '@monorepo/expo/shared/static';
import { BasicModal, BodyText, H1 } from '@monorepo/expo/shared/ui-components';
import { useState } from 'react';
import { Pressable } from 'react-native';

export default function InfoModal() {
  const [visible, setVisible] = useState(false);

  const showModal = () => {
    setVisible(true);
  };

  return (
    <>
      <Pressable
        style={{ marginLeft: Spacings.xs }}
        onPress={showModal}
        accessible
        accessibilityLabel="Public note information"
        accessibilityHint="information about public note"
      >
        <InfoIcon size="sm" color={Colors.PRIMARY_EXTRA_DARK} />
      </Pressable>
      <BasicModal visible={visible} setVisible={setVisible}>
        <H1 mb="sm">About Public Note</H1>
        <BodyText>
          Public Note can be integrated to HMIS. LAHSA prefers you to enter in
          G.I.R.P method. G for Goal, I for Intervention, R for Response, and P
          for Planning. Please enter information by following the method.
        </BodyText>
      </BasicModal>
    </>
  );
}